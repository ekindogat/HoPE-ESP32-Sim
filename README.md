# HoPE-MQTT-Project
Home Planet Environmental Monitoring System Project - A real-time sensor monitoring dashboard using MQTT for wireless communication.

## Overview
This project implements a real-time monitoring system for environmental sensors (temperature, humidity, and light intensity) using MQTT protocol. It features a modern, responsive web dashboard that displays sensor data with status indicators and alerts.

### Features
- Real-time sensor data monitoring
- Status indicators for ideal, warning, and critical conditions
- Responsive web dashboard with modern UI
- Automatic alerts for critical and warning conditions
- Connection status monitoring
- Simulated sensor data generation for testing
- MQTT-based wireless communication

## Requirements
### Software
- Python 3.x
- pip (Python package manager)

### Python Packages
Install the required packages using pip:
```bash
pip install flask paho-mqtt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ekindogat/HoPE-MQTT-Project
cd HoPE-MQTT-Project
```

2. Install the required Python packages using this command:
```bash
pip install flask paho-mqtt
```

## Project Structure
```
HoPE-MQTT-Project/
├── app.py                 # Flask application and main entry point
├── mqtt_client.py         # MQTT client implementation
├── static/               # Static files
│   ├── css/             # CSS stylesheets
│   └── icon/            # Project icons
├── HoPE Sensors.url       # Wokwi simulator
└── templates/            # HTML templates
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Access the dashboard:
   - Open a web browser
   - Navigate to `http://localhost:5000`
   - The dashboard will automatically connect to the MQTT broker and start displaying sensor data

### Sensor Data Ranges
The system monitors three environmental parameters with the following ranges:

#### Temperature
- Ideal: 15-30°C
- Warning: 5°C range for minimum and maximum ideal value
- Critical: <10°C or >35°C

#### Humidity
- Ideal: 30-50%
- Warning: 10% range for minimum and maximum ideal value
- Critical: <20% or >60%

#### Light Intensity
- Ideal: 20-30k lux
- Warning: 10k lux range for minimum and maximum ideal value
- Critical: <10k or >40k lux

## Development
- The dashboard updates every 2 seconds
- Sensor data includes timestamps to prevent alert spamming
- The system automatically handles connection issues and reconnection
- Critical alerts persist until resolved, while warning alerts clear with new data

## Testing
The project includes a simulated sensor data generator for testing purposes. It can generate:
- Random values within defined ranges
- Simulated sensor failures
- Network delays and connection issues

## License
