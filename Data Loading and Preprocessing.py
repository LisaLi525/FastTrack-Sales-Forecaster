import pandas as pd
import numpy as np
import itertools
import statsmodels.api as sm

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['Month'] = pd.to_datetime(df['Month'])
    df = df.set_index('Month')
    return df
