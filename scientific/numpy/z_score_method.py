
import pandas as pd
import numpy as np

def outliers_iqr(ys):

    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)

    return np.where((ys > upper_bound) | (ys < lower_bound))
