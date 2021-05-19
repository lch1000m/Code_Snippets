import pandas as pd
import numpy as np


sp = pd.DataFrame(
    {
        'A': ['a', 'b', 'c'],
        'B': ['A', 'A' , 'A'],
        'C': [0, 50, 100],
    }
)

sample = [0, 0.15,0.95,1]


_perc = 0.15
_p = "P" + str(int(_perc*100))

pivot = pd.pivot_table(
    sp,
    index=['B'],
    values='C',
    aggfunc= lambda x: np.percentile(x, _perc),
)

print(pivot)

print('End')
