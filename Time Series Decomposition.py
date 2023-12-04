def decompose_time_series(series, model='additive'):
    decomposition = sm.tsa.seasonal_decompose(series, model=model)
    return decomposition
