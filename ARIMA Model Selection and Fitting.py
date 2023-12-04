def select_and_fit_arima_model(time_series, p_values, d_values, q_values, s_value):
    pdq = list(itertools.product(p_values, d_values, q_values))
    seasonal_pdq = [(x[0], x[1], x[2], s_value) for x in pdq]
    best_aic = np.inf
    best_pdq = None
    best_seasonal_pdq = None
    best_model = None

    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                model = sm.tsa.statespace.SARIMAX(time_series,
                                                  order=param,
                                                  seasonal_order=param_seasonal,
                                                  enforce_stationarity=False,
                                                  enforce_invertibility=False)
                results = model.fit()
                if results.aic < best_aic:
                    best_aic = results.aic
                    best_pdq = param
                    best_seasonal_pdq = param_seasonal
                    best_model = results
            except:
                continue

    return best_model, best_pdq, best_seasonal_pdq
