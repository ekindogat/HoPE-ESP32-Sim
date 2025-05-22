import network
import time
import ujson
from umqtt.simple import MQTTClient
import ntptime
import random

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "wokwi/sensors/data"
MQTT_USER = ""
MQTT_PASSWORD = ""

# Sensor value ranges for testing different conditions
TEMP_RANGES = {
    'critical_low': (0, 5),      # Critical low: 0-5°C
    'warning_low': (5, 10),      # Warning low: 5-10°C
    'ideal_low': (15, 20),       # Ideal low: 15-20°C
    'ideal_high': (25, 30),      # Ideal high: 25-30°C
    'warning_high': (35, 40),    # Warning high: 35-40°C
    'critical_high': (40, 45)    # Critical high: 40-45°C
}

HUMIDITY_RANGES = {
    'critical_low': (0, 15),     # Critical low: 0-15%
    'warning_low': (15, 20),     # Warning low: 15-20%
    'ideal_low': (30, 35),       # Ideal low: 30-35%
    'ideal_high': (45, 50),      # Ideal high: 45-50%
    'warning_high': (70, 75),    # Warning high: 70-75%
    'critical_high': (80, 85)    # Critical high: 80-85%
}

LIGHT_RANGES = {
    'critical_low': (0, 5000),           # Critical low: 0-5000 lux
    'warning_low': (5000, 10000),        # Warning low: 5000-10000 lux
    'ideal_low': (20000, 25000),         # Ideal low: 20000-25000 lux
    'ideal_high': (25000, 30000),        # Ideal high: 25000-30000 lux
    'warning_high': (40000, 45000),      # Warning high: 40000-45000 lux
    'critical_high': (45000, 50000)      # Critical high: 45000-50000 lux
}

def get_random_value(ranges):
    """Get a random value from a randomly selected range."""
    condition = random.choice(list(ranges.keys()))
    min_val, max_val = ranges[condition]
    return round(random.uniform(min_val, max_val), 1)

def generate_sensor_data():
    """Generate random sensor data that tests all conditions."""
    timestamp = get_timestamp()
    return {
        "timestamp": timestamp,
        "temp": get_random_value(TEMP_RANGES),
        "humidity": get_random_value(HUMIDITY_RANGES),
        "light_intensity": int(get_random_value(LIGHT_RANGES))
    }

# Wi-Fi connection
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

# Set up NTP for time synchronization
ntptime.settime()  # Synchronize with NTP server

# MQTT connection
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()
print("Connected!")

def get_timestamp():
    """Get the current time formatted as a timestamp."""
    t = time.localtime()
    return "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Counter to occasionally simulate sensor failure
sensor_failure_counter = 0

while True:
    try:
        # Get current time for timestamp
        timestamp = get_timestamp()
        
        # Simulate occasional sensor failure (every ~30 readings)
        sensor_failure_counter += 1
        if sensor_failure_counter >= 30:
            sensor_data = {
                "timestamp": timestamp,
                "temp": None,  # Simulate sensor failure
                "humidity": get_random_value(HUMIDITY_RANGES),
                "light_intensity": int(get_random_value(LIGHT_RANGES))
            }
            sensor_failure_counter = 0
            print("Simulating temperature sensor failure")
        else:
            sensor_data = generate_sensor_data()
        
        # Format the message with the data
        message = ujson.dumps(sensor_data)

        # Print data in the specified format on the serial monitor
        if sensor_data["temp"] is not None:
            print("Timestamp: {}, Temperature: {:.1f}°C, Humidity: {:.1f}%, Light Intensity: {}".format(
                sensor_data["timestamp"], sensor_data["temp"], sensor_data["humidity"], sensor_data["light_intensity"]))
        else:
            print("Timestamp: {}, Temperature: N/A, Humidity: {:.1f}%, Light Intensity: {}".format(
                sensor_data["timestamp"], sensor_data["humidity"], sensor_data["light_intensity"]))

        # Publish to MQTT
        print(f"Reporting to MQTT topic {MQTT_TOPIC}: {message}")
        client.publish(MQTT_TOPIC, message)
        
        # Random delay between 2-4 seconds to simulate real sensor behavior
        time.sleep(random.uniform(2, 4))
        
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(5)  # Wait longer on error
        try:
            # Try to reconnect to MQTT
            client.disconnect()
            client.connect()
        except:
            pass