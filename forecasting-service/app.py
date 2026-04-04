from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json["values"]
    
    # simple moving average
    forecast_value = np.mean(data[-5:])
    
    return jsonify({"forecast": forecast_value})

if __name__ == "__main__":
    app.run(port=5001)