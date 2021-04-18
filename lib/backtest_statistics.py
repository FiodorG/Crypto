import pandas as pd
import numpy as np


def sharpe(df: pd.DataFrame) -> float:
    mean = df.mean()
    std = df.std()
    return np.sqrt(252) * mean / std


def rolling_sharpe(df: pd.DataFrame, window: int) -> float:
    mean = df.rolling(window).mean()
    std = df.rolling(window).std()
    return np.sqrt(252) * mean / std
