import json
from kafka import KafkaConsumer
import requests

consumer = KafkaConsumer(
    "metrics-stream",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

buffer = []

for msg in consumer:
    event = msg.value
    buffer.append(event["cpu"])

    if len(buffer) >= 5:
        # call forecasting
        requests.post("http://localhost:5001/forecast", json={"values": buffer})

        # call anomaly
        requests.post("http://localhost:5002/anomaly", json={"values": buffer})

        buffer = []