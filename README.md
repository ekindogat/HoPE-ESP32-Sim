# HoPE-MQTT-Project
Home Planet Environmental Monitoring System Project, a basic wireless communication simulator project. 

## Requirements:
 - Python, PIP
 - Python libraries: paho-mqtt, flask

<br>

## Installation:
- Instal [Python 3](https://www.python.org/downloads/)
- Install python packages by this command
> pip install flask paho-mqtt

### Start:
 - Start "app.py"
 - (TO BE EDITED) 
 - This will start the subscriptor reading messages sent by ESP32 by subscribing the MQTT channel.
 - Then:
     - Go to http://localhost:{port}/ui (depending on the what port the server listens at, currently 1883) in a web browser on the same network.