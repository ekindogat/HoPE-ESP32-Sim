import paho.mqtt.client as mqtt
import time
import json

# Shared data dictionary to store latest values
sensor_data = {"temp": None, "humidity": None, "light_intensity": None, "timestamp": None}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        print("Successfully connected to MQTT broker")
        client.subscribe("wokwi/sensors/data")
    else:
        print(f"Failed to connect, return code {rc}")
        # Try to reconnect
        time.sleep(5)
        client.reconnect()

def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")
    if rc != 0:
        print("Unexpected disconnection. Attempting to reconnect...")
        try:
            client.reconnect()
        except:
            pass

def on_message(client, userdata, msg):
    try:
        # payload format: {"temp": val, "humidity": val, "light_intensity": val, "timestamp": val}
        data = json.loads(msg.payload.decode())
        # Update timestamp if not present
        if "timestamp" not in data:
            data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
        # Update sensor data
        sensor_data.update(data)
        print(f"Received data: {data}")
    except Exception as e:
        print("Failed to parse message:", e)

# Create MQTT client with automatic reconnect
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Enable automatic reconnect
client.reconnect_delay_set(min_delay=1, max_delay=60)

def start_mqtt():
    try:
        client.connect("test.mosquitto.org", 1883, 60)
        client.loop_start()  # non-blocking
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        # Try to reconnect after a delay
        time.sleep(5)
        start_mqtt()
