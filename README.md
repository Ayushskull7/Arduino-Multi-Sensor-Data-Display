# Arduino-Multi-Sensor-Data-Display
This project reads data from multiple sensors connected to an Arduino and displays it in a Python GUI. It supports:

Ultrasonic Sensor (HC-SR04) for measuring distance.
DHT11 Sensor for temperature and humidity.
Soil Moisture Sensor for soil moisture level.
IR Sensor for detecting nearby objects. [🛠️]
The Arduino sends sensor data over Serial to the Python app, which shows real-time values. Select a sensor in the GUI to view its data, and see live updates or a message if no data is detected.