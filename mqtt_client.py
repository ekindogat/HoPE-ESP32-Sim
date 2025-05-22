import paho.mqtt.client as mqtt

# Shared data dictionary to store latest values
sensor_data = {"temp": None, "humidity": None, "light_intensity": None}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("wokwi/sensors/data")

def on_message(client, userdata, msg):
    try:
        # payload format: {"temp": val, "humidity": val, "light_intensity": val}
        import json
        data = json.loads(msg.payload.decode())
        # debug
        print(data)
        sensor_data.update(data)
    except Exception as e:
        print("Failed to parse message:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt():
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()  # non-blocking
