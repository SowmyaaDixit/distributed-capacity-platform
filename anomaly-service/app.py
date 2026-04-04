from flask import Flask, request, jsonify
from detect import detect_anomaly

app = Flask(__name__)

@app.route("/anomaly", methods=["POST"])
def anomaly():
    values = request.json["values"]

    result = detect_anomaly(values)

    print("Anomaly result:", result)

    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5002)