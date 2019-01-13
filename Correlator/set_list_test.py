# set_list class test

import pandas as pd

import goldentiger as gt




def test(expr):
    df = pd.DataFrame({
        'A':[1,2,3,'lot_wf'],
        'B':['a','ab','ca','d'],
    })

    res = eval(expr)

    return res



if __name__ == '__main__':


    _values = ['lot_wf']

    exp = "df[(df['B'].str.contains('a')) & (df['B'].str.startswith('c'))]"

    res = test(exp)

    print(res)
