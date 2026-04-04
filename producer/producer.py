from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "capacity-events"

def generate_event():
    return {
        "timestamp": time.time(),
        "service": "api",
        "cpu_usage": random.randint(10, 100),
        "request_count": random.randint(50, 500)
    }

while True:
    event = generate_event()
    producer.send(TOPIC, event)
    print(f"Produced: {event}")
    time.sleep(1)