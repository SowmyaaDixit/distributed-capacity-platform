import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

services = ["auth", "payments", "search"]

def generate_event():
    return {
        "service": random.choice(services),
        "timestamp": int(time.time()),
        "cpu": random.randint(40, 95),
        "latency": random.randint(50, 300)
    }

while True:
    event = generate_event()
    producer.send("metrics-stream", event)
    print("Sent:", event)
    time.sleep(1)