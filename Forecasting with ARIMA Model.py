def forecast_with_arima(model, steps):
    forecast = model.get_forecast(steps=steps)
    return forecast.predicted_mean, forecast.conf_int()
