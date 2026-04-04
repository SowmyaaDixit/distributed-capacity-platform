from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(
    'capacity-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def process_event(event):
    latency = time.time() - event["timestamp"]
    
    print(f"Processing event | latency={latency:.3f}s")

    # Simple anomaly detection
    if event["cpu_usage"] > 85:
        print("⚠️ High CPU anomaly detected")

    return latency

def safe_consume():
    for message in consumer:
        for attempt in range(3):  # at‑least‑once attempt
            try:
                process_event(message.value)
                consumer.commit()  # manual commit only on success
                break  # success
            except Exception as e:
                print(f"Error: {e}, retrying {attempt+1}/3")
                time.sleep(2 ** attempt)
        else:
            # if we get here, all retries failed
            print("💥 failed after retries — sending to dead‑letter queue")
            # optionally send to a DLQ topic for later inspection

if __name__ == "__main__":
    safe_consume()