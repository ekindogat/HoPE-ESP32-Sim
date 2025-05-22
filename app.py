from flask import Flask, render_template, jsonify
from mqtt_client import start_mqtt, sensor_data

app = Flask(__name__, static_folder='css', template_folder='templates')
start_mqtt()

@app.route("/")
def dashboard():
    return render_template("realtime_dashboard.html")

@app.route("/data")
def data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(debug=True)

""" LAVENDER IDEAL CONDITION
Temperature: 15–30°C (ideal), <10°C or >35°C (critical)

Humidity: 30–50% (ideal), <20% or >70% (critical)

Light Intensity: 20000–30000 lux (ideal), <10000 or >40000 lux (critical)

"""