def detect_anomaly(values, threshold=2.0):
    if not values or len(values) < 2:
        return {
            "anomaly": False,
            "reason": "not enough data"
        }

    mean = sum(values) / len(values)

    variance = sum((x - mean) ** 2 for x in values) / len(values)
    std = variance ** 0.5

    latest = values[-1]

    z_score = (latest - mean) / std if std > 0 else 0

    is_anomaly = abs(z_score) > threshold

    return {
        "anomaly": is_anomaly,
        "z_score": round(z_score, 3),
        "mean": round(mean, 2),
        "std": round(std, 2),
        "latest": latest
    }