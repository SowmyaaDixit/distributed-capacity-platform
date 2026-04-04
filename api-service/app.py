# api-service/app.py
from flask import Flask, jsonify
from utils.metrics import record_success, record_failure, report
from kafka import KafkaConsumer
import json
import time
import threading

app = Flask(__name__)

# -------------------- Flask endpoints --------------------
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/metrics")
def metrics_route():
    return jsonify(report())

# -------------------- Kafka consumer --------------------
consumer = KafkaConsumer(
    'capacity-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=False  # manual commit for reliability
)

def process_event(event):
    start = time.time()
    try:
        latency = time.time() - event["timestamp"]
        print(f"Processing event | latency={latency:.3f}s")
        
        # Anomaly detection
        if event["cpu_usage"] > 85:
            print("⚠️ High CPU anomaly detected")

        # record metrics
        record_success(latency * 1000)  # milliseconds
        return latency
    except Exception:
        record_failure()
        raise

def safe_consume():
    for message in consumer:
        for attempt in range(3):
            try:
                process_event(message.value)
                consumer.commit()  # commit only on success
                break
            except Exception as e:
                print(f"Error: {e}, retrying {attempt+1}/3")
                time.sleep(2 ** attempt)
        else:
            print("💥 failed after retries — consider sending to DLQ")

# -------------------- Run consumer in background --------------------
def start_consumer():
    thread = threading.Thread(target=safe_consume, daemon=True)
    thread.start()

# -------------------- Start Flask + consumer --------------------
if __name__ == "__main__":
    start_consumer()
    app.run(host="0.0.0.0", port=5000)