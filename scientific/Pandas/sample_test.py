
import pandas as pd, numpy as np

from datetime import datetime as dt


condition = {
    'and':[
        {
            'stepA':['PPID',['ppid_a']],
        },
        {
            'stepB':['EQP_ID',['eqpid_b']],
        }
    ],
}


for key, val in condition.items():
    if key == 'and':
        for val2 in val:
            for key2, val2 in val2.items():
                print('{0} - {1}'.format(key2, val2))
