from functools import partial
from typing import Literal

import numpy as np
import sklearn
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, f1_score


def mean_error(y_true, y_est) -> float:
    return float(np.mean(y_est - y_true))


def rmse(y_true, y_est):
    if sklearn.__version__ >= '1.4':
        from sklearn.metrics import root_mean_squared_error
        return root_mean_squared_error(y_true, y_est)
    else:
        mse = mean_squared_error(y_true, y_est)
        return np.sqrt(mse)


def moe_95(y_true, y_est, metric: Literal["moe", "lo", "hi"] = 'moe') -> float:
    me = mean_error(y_true, y_est)
    rmse_value = rmse(y_true, y_est)
    if metric == 'lo':
        res = me - (rmse_value * 1.96)
    elif metric == 'hi':
        res = me + (rmse_value * 1.96)
    elif metric == 'moe':
        res = np.mean([(np.abs(me - (rmse_value * 1.96))), (me + (rmse_value * 1.96))])
    else:
        raise KeyError(f'Invalid metric supplied.  Allowed values are: {Literal["moe", "lo", "hi"]}')
    return res


def r2(y_true, y_est):
    ssr = ((y_true - y_est) ** 2).sum()
    sst = ((y_true - y_true.mean()) ** 2).sum()
    return 1 - (ssr / sst)


def r2_with_nan(y_true, y_est):
    numerator = np.nansum((y_true - y_est) ** 2, axis=0, dtype=np.float64)
    denominator = np.nansum((y_true - np.nanmean(y_true, axis=0)) ** 2, axis=0, dtype=np.float64)
    return np.mean(1 - numerator / denominator)


regression_metrics = {
    # 'r2_nan': r2_with_nan,
    'r2_score': r2_score,
    'me': mean_error,
    'r2': r2,
    'mae': mean_absolute_error,
    'mse': mean_squared_error,
    'rmse': rmse,
    'moe': partial(moe_95, metric='moe'),
    'moe_lo': partial(moe_95, metric='lo'),
    'moe_hi': partial(moe_95, metric='hi')}

classification_metrics = {'f1': f1_score}
