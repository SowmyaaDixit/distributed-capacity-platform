def forecast_load(history):
    if len(history) < 5:
        return sum(history) / len(history)

    # simple moving average
    return sum(history[-5:]) / 5