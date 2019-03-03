# eval test

import os

import pandas as pd, goldentiger as gt


df = pd.read_excel(
    os.path.join(gt.sample, 'sample.xlsx'),
    sheetname='',
)
