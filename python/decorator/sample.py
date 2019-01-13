# decorator test for remove columns

import functools

import pandas as pd


if __name__ == '__main__':

    df = pd.read_excel(
        r'C:\Codes\Snippets\sample data\aliasing.xlsx',
        sheetname='alias',
    )

    option = [
        'iutk2.5p',
        'iutk2.5',
    ]

    alias = [
        'iUTK2.5++',
        'iUTK2.5',
        'Other',
    ]

    for i, it in enumerate(option):
        print('input {0} - {1}'.format(i, it))
        if i == 0:  # 1st element
            df.loc[df['ppid'].str.contains(it), 'ALIAS'] = alias[i]
        else:   # not a 1st element
            df.loc[(df['ppid'].str.contains(it)) & (df['ALIAS'].isnull()), 'ALIAS'] = alias[i]

    df.loc[df['ALIAS'].isnull(), 'ALIAS'] = alias[len(alias)-1]


    print(df)
