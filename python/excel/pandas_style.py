# pandas styler

import os

import pandas as pd
import goldentiger as gt
import seaborn as sns


filepath = r'C:\Codes\Snippets\sample data\pandas style.xlsx'

df = pd.read_excel(
    gt.sample,
    sheetname='wip',
)

cm = sns.light_palette("green", as_cmap=True)
df.style.background_gradient(cmap=cm)

df.to_excel(filepath, sheet_name='pandas')

os.startfile(filepath)
