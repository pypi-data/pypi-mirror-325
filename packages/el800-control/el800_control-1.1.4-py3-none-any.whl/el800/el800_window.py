import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import serial
import serial.tools.list_ports
import csv
import os
from datetime import datetime


READ_COMMAND = b'D'


def extract_string(data):
    try:
        # Ensure data is binary-safe
        start_index = 2
        end_keyword = b'\x1A\x1E'
        # Find the position of the keyword 'ASSAY'
        end_index = data.find(end_keyword)

        if end_index == -1:
            data_len = len(data)
            raise ValueError(f"Keyword '0x1A0x1E' not found in data len={data_len}.")

        # Extract the substring from position 2 to the keyword
        result = data[start_index:end_index].decode('ascii', errors='ignore')
        return result

    except Exception as e:
        print(f"Error during string extraction: {e}")
        return None


def csv_to_matrix(csv_string):
    """
    Converts a string of comma-separated values into a matrix of numbers, ignoring the first value before the first comma on each line.

    Args:
        csv_string (str): The input string containing lines of comma-separated values.

    Returns:
        list[list[float]]: A matrix where each inner list represents a row of numbers.
    """
    try:
        # Split the string into lines
        lines = csv_string.strip().split('\n')

        # Convert each line into a list of floats, ignoring the first value (empty or not)
        matrix = [list(map(float, line.split(',')[1:])) for line in lines if line.strip()]

        return [[element / 1000 if isinstance(element, (float, int)) else element for element in row] for row in matrix]

    except ValueError as e:
        print(f"Error converting string to matrix: {e}")
        return None

class PlateReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EL800 96-Well Plate Reader")
        self.serial_connection = None

        # Serial port settings
        self.serial_frame = tk.Frame(self.root)
        self.serial_frame.pack(pady=5)

        tk.Label(self.serial_frame, text="Serial Port:").grid(row=0, column=0, padx=5)
        self.serial_port_combo = ttk.Combobox(self.serial_frame, width=15, state='readonly')
        self.serial_port_combo.grid(row=0, column=1, padx=5)
        self.populate_serial_ports()        

        tk.Label(self.serial_frame, text="Baud Rate:").grid(row=0, column=2, padx=5)
        self.baud_rate_combo = ttk.Combobox(
            self.serial_frame, width=10, values=[300, 1200, 2400, 4800, 9600, 19200]
        )
        self.baud_rate_combo.grid(row=0, column=3, padx=5)
        self.baud_rate_combo.set(9600)  # Default value

        tk.Label(self.serial_frame, text="Data Bits:").grid(row=1, column=0, padx=5)
        self.databits_combo = ttk.Combobox(self.serial_frame, width=10, values=[7, 8])
        self.databits_combo.grid(row=1, column=1, padx=5)
        self.databits_combo.set(8)  # Default value

        tk.Label(self.serial_frame, text="Parity:").grid(row=1, column=2, padx=5)
        self.parity_combo = ttk.Combobox(self.serial_frame, width=10, values=["No", "Even", "Odd"])
        self.parity_combo.grid(row=1, column=3, padx=5)
        self.parity_combo.set("No")  # Default value

        tk.Label(self.serial_frame, text="Stop Bits:").grid(row=2, column=0, padx=5)
        self.stopbits_combo = ttk.Combobox(self.serial_frame, width=10, values=[1, 2])
        self.stopbits_combo.grid(row=2, column=1, padx=5)
        self.stopbits_combo.set(1)  # Default value

        tk.Label(self.serial_frame, text="Handshake:").grid(row=2, column=2, padx=5)
        self.handshake_combo = ttk.Combobox(
            self.serial_frame, width=15, values=["No", "XON/XOFF", "RTS", "XON/XOFF+RTS"]
        )
        self.handshake_combo.grid(row=2, column=3, padx=5)
        self.handshake_combo.set("No")  # Default value

        self.reconnect_button = tk.Button(self.serial_frame, text="(Re)connect", command=self.reconnect_serial)
        self.reconnect_button.grid(row=0, column=4, padx=5)

        # 96-well plate grid
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(pady=10)

        # Add headers
        for col in range(12):
            tk.Label(
                self.grid_frame, text=f"{col + 1}", width=8, relief="ridge", bg="lightgray"
            ).grid(row=0, column=col + 1, padx=2, pady=2)

        for row in range(8):
            tk.Label(
                self.grid_frame, text=chr(65 + row), width=8, relief="ridge", bg="lightgray"
            ).grid(row=row + 1, column=0, padx=2, pady=2)

        self.well_labels = []
        for row in range(8):  # Rows A-H
            row_labels = []
            for col in range(12):  # Columns 1-12
                label = tk.Label(
                    self.grid_frame,
                    text="0.000",  # Default OD600 value
                    width=8,
                    height=2,
                    relief="ridge",
                    bg="white"
                )
                label.grid(row=row + 1, column=col + 1, padx=2, pady=2)
                row_labels.append(label)
            self.well_labels.append(row_labels)

        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.read_button = tk.Button(
            self.button_frame, text="Read", command=self.read_od600_values
        )
        self.read_button.pack(side="left", padx=5)

        self.close_button = tk.Button(
            self.button_frame, text="Close", command=self.root.quit
        )
        self.close_button.pack(side="left", padx=5)

        # Directory selector
        self.directory_frame = tk.Frame(self.root)
        self.directory_frame.pack(pady=10)

        tk.Label(self.directory_frame, text="Save Directory:").pack(side="left", padx=5)
        self.directory_entry = tk.Entry(self.directory_frame, width=40)
        self.directory_entry.pack(side="left", padx=5)
        self.browse_button = tk.Button(
            self.directory_frame, text="Browse", command=self.browse_directory
        )
        self.browse_button.pack(side="left", padx=5)

        directory = os.path.expanduser("~")
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)

        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
          
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
  

    def populate_serial_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        if ports:
            self.serial_port_combo['values'] = ports
            self.serial_port_combo.current(0)
        else:
            self.serial_port_combo['values'] = ["No ports found"]
            self.serial_port_combo.current(0)

    def communicate_with_serial(self):
        try:
            with self.serial_connection as ser:
    
                # Send binary value 0x11
                ser.write(READ_COMMAND)
                print("Sent: 'D'")
    
                # Receive multiline string
                print("Receiving data...")
                received_data = extract_string(ser.read(657))
                ser.reset_input_buffer()
    
                print("Received data:")
                print(received_data)
                return received_data
    
        except serial.SerialException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def read_od600_values(self):
        # Communicate with the serial device
        try:
            if not self.serial_connection:
                self.reconnect_serial()
                
            data = self.communicate_with_serial()

            if data:
                # Convert the received CSV data to a matrix
                matrix = csv_to_matrix(data)
                if matrix:
                    for row_idx, row in enumerate(matrix):
                        for col_idx, value in enumerate(row):
                            if row_idx < 8 and col_idx < 12:  # Ensure valid well range
                                self.well_labels[row_idx][col_idx].config(text=f"{value:.3f}")
                    self.save_to_csv(matrix)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read OD600 values: {e}")

    def save_to_csv(self, matrix):
        directory = self.directory_entry.get().strip()
        if not directory:
            messagebox.showwarning("Warning", "No save directory selected. Data will not be saved.")
            return
    
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"plate_{timestamp}.csv"
        filepath = os.path.join(directory, filename)
    
        try:
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([" "] + [str(i) for i in range(1, 13)])  # Column headers
                
                for row_idx, row in enumerate(matrix):
                    writer.writerow([chr(65 + row_idx)] + [f"{value:.3f}" for value in row])
    
                self.status_bar.config(text=f"Data saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if not directory:
            directory = os.path.expanduser("~")
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)

    def reconnect_serial(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed.")

        # Get serial port settings from UI
        port = self.serial_port_combo.get()
        baudrate = int(self.baud_rate_combo.get())
        bytesize = serial.EIGHTBITS if self.databits_combo.get() == "8" else serial.SEVENBITS
        stopbits = serial.STOPBITS_TWO if self.stopbits_combo.get() == "2" else serial.STOPBITS_ONE
        parity = {
            "No": serial.PARITY_NONE,
            "Even": serial.PARITY_EVEN,
            "Odd": serial.PARITY_ODD
        }[self.parity_combo.get()]
        timeout=5
        
        try:
            self.serial_connection = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize,
            stopbits=stopbits,
            parity=parity,
            timeout=timeout)
            print(f"Connected to {port}")
        except serial.SerialException as e:
            messagebox.showerror("Error", f"Failed to open serial port: {e}")

    def on_close(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Serial connection closed on exit.")
        self.root.destroy()

def gui():
    root = tk.Tk()
    PlateReaderApp(root)
    root.mainloop()
        
if __name__ == "__main__":
    gui()
