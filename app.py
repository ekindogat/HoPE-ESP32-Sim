from flask import Flask, render_template, jsonify
from mqtt_client import start_mqtt, sensor_data

app = Flask(__name__)
start_mqtt()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(debug=True)
