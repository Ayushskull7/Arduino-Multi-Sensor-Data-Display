import tkinter as tk
from tkinter import ttk
import serial
import threading

arduinoData = serial.Serial('COM8', 9600)
arduinoData.timeout = 1

root = tk.Tk()
root.title("Sensor Data")
root.geometry("700x600")
root.configure(bg="#f7f7f7")

temperature = tk.StringVar()
humidity = tk.StringVar()
percentvalue = tk.StringVar()
ir_value = tk.StringVar()
ultrasonic_value = tk.StringVar()
selected_sensor = tk.StringVar(value="Temperature")


def arduino():
    while True:
        try:
            raw_data = arduinoData.readline().decode('utf-8', errors='ignore').strip()
            if raw_data:
                if raw_data.startswith("Temperature:"):
                    temperature.set(raw_data.split(":")[1])
                elif raw_data.startswith("Humidity:"):
                    humidity.set(raw_data.split(":")[1])
                elif raw_data.startswith("Percentvalue:"):
                    percentvalue.set(raw_data.split(":")[1])
                elif raw_data.startswith("IR:"):
                    ir_value.set(raw_data.split(":")[1])
                elif raw_data.startswith("Ultrasonic Distance:"):
                    ultrasonic_value.set(raw_data.split(":")[1])
                update_raw_data_display(raw_data)

        except Exception as e:
            print(f"Error reading data: {e}")


def update_raw_data_display(raw_data):
    if selected_sensor.get() == "Temperature" and raw_data.startswith("Temperature:"):
        raw_data_display.insert(tk.END, f"{raw_data}\n")
    elif selected_sensor.get() == "Humidity" and raw_data.startswith("Humidity:"):
        raw_data_display.insert(tk.END, f"{raw_data}\n")
    elif selected_sensor.get() == "Soil Moisture" and raw_data.startswith("Percentvalue:"):
        raw_data_display.insert(tk.END, f"{raw_data}\n")
    elif selected_sensor.get() == "IR Sensor" and raw_data.startswith("IR:"):
        raw_data_display.insert(tk.END, f"{raw_data}\n")
    elif selected_sensor.get() == "Ultrasonic Sensor" and raw_data.startswith("Ultrasonic Distance:"):
        raw_data_display.insert(tk.END, f"{raw_data}\n")

    raw_data_display.see(tk.END)


def update_display(*args):
    if selected_sensor.get() == "Temperature":
        value = temperature.get() if temperature.get() else "Sensor not connected or no incoming data"
        display_value.set(f"Temperature: {value} °C")
    elif selected_sensor.get() == "Humidity":
        value = humidity.get() if humidity.get() else "Sensor not connected or no incoming data"
        display_value.set(f"Humidity: {value} %")
    elif selected_sensor.get() == "Soil Moisture":
        value = percentvalue.get() if percentvalue.get() else "Sensor not connected or no incoming data"
        display_value.set(f"Soil Moisture: {value} %")
    elif selected_sensor.get() == "IR Sensor":
        value = ir_value.get() if ir_value.get() else "Sensor not connected or no incoming data"
        display_value.set(f"IR Sensor: {value}")
    elif selected_sensor.get() == "Ultrasonic Sensor":
        value = ultrasonic_value.get() if ultrasonic_value.get() else "Sensor not connected or no incoming data"
        display_value.set(f"Ultrasonic Distance: {value} cm")

    root.after(2000, update_display)


display_value = tk.StringVar()
previous_sensor = selected_sensor.get()


def sensor_changed(*args):
    global previous_sensor
    if selected_sensor.get() != previous_sensor:
        raw_data_display.delete(1.0, tk.END)
        previous_sensor = selected_sensor.get()
    update_display()


selected_sensor.trace_add("write", sensor_changed)

menu_label = tk.Label(root, text="Select Sensor:", font=('Helvetica', 12), bg="#f7f7f7", fg="#333")
menu_label.pack(pady=5)

sensor_menu = ttk.Combobox(root, textvariable=selected_sensor, font=('Helvetica', 12),
                           values=["Temperature", "Humidity", "Soil Moisture", "IR Sensor", "Ultrasonic Sensor"],
                           state="readonly")
sensor_menu.pack(pady=5)

data_label = tk.Label(root, textvariable=display_value, font=('Helvetica', 16, 'bold'),
                      bg="#f7f7f7", fg="#4a4a4a")
data_label.pack(pady=20)

raw_data_label = tk.Label(root, text="Raw Sensor Data:", font=('Helvetica', 12),
                          bg="#f7f7f7", fg="#333")
raw_data_label.pack(pady=5)

raw_data_display = tk.Text(root, height=15, width=70, font=('Helvetica', 10),
                           bg="#eaeaea", fg="#333")
raw_data_display.pack(pady=5)
raw_data_display.config(state=tk.NORMAL)

threading.Thread(target=arduino, daemon=True).start()
update_display()

root.mainloop()
