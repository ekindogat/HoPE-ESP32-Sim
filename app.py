from flask import Flask, render_template, jsonify, send_from_directory
from mqtt_client import start_mqtt, sensor_data
import os

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates')

# Create static folder structure
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/icon', exist_ok=True)

start_mqtt()

@app.route("/")
def dashboard():
    return render_template("realtime_dashboard.html")

@app.route("/data")
def data():
    return jsonify(sensor_data)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)

""" LAVENDER IDEAL CONDITION
Temperature: 15–30°C (ideal), <10°C or >35°C (critical)

Humidity: 30–50% (ideal), <20% or >70% (critical)

Light Intensity: 20000–30000 lux (ideal), <10000 or >40000 lux (critical)

"""