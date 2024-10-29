# Arduino Multi-Sensor Data Display

This project reads data from multiple sensors connected to an Arduino and displays it in a Python GUI application. It supports:

- **Ultrasonic Sensor (HC-SR04)**: Measures distance to nearby objects.
- **DHT11 Sensor**: Captures temperature and humidity.
- **Soil Moisture Sensor**: Measures soil moisture level.
- **IR Sensor**: Detects nearby objects or obstacles. [🛠️]

The Arduino collects data from each sensor and sends it over Serial to the Python GUI. Select a sensor in the GUI to view its data in real-time. If no data is detected, the interface will show a message indicating "Sensor Not Connected" or "No Incoming Data."

---

**Key Features**  
- **Real-time Data Display**: View live sensor readings based on your selected sensor.
- **Multi-Sensor Support**: Easily switch between sensors to monitor different environmental parameters.
- **Connection Status Indicator**: Shows if data is not available or if a sensor is disconnected.
