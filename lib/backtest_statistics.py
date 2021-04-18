import pandas as pd
import numpy as np

from .constants import DAYS_IN_YEAR


def account_curve_statistics(acc_curve: pd.DataFrame):
    stats = {
        "Mean $Return": acc_curve.diff().mean() * DAYS_IN_YEAR,
        "Stddev $Return": acc_curve.diff().std() * np.sqrt(DAYS_IN_YEAR),
        "Sharpe": sharpe(acc_curve),
    }
    return pd.Series(stats)


def sharpe(acc_curve: pd.DataFrame) -> float:
    mean = acc_curve.diff().mean()
    std = acc_curve.diff().std()
    return np.sqrt(DAYS_IN_YEAR) * mean / std


def rolling_sharpe(acc_curve: pd.DataFrame, window: int) -> float:
    mean = acc_curve.diff().rolling(window).mean()
    std = acc_curve.diff().rolling(window).std()
    return np.sqrt(DAYS_IN_YEAR) * mean / std
