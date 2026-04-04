metrics = {
    "events_processed": 0,
    "events_failed": 0,
    "total_latency_ms": 0,
}

def record_success(latency_ms):
    metrics["events_processed"] += 1
    metrics["total_latency_ms"] += latency_ms

def record_failure():
    metrics["events_failed"] += 1

def report():
    avg_latency = (
        metrics["total_latency_ms"] / metrics["events_processed"]
        if metrics["events_processed"] else 0
    )
    return {
        "processed": metrics["events_processed"],
        "failures": metrics["events_failed"],
        "avg_latency_ms": avg_latency,
    }