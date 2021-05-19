# aggfunc 만들기

import goldentiger as gt
import pandas as pd


def concat(a, b, *args, **kwargs):

    if a.empty:
        return b

    else:
        res = pd.concat([a, b], *args, **kwargs)

        return res


def make_aggfunc(df, option):

    res = pd.DataFrame()

    if 'avg' in option:

        _df = pd.pivot_table(
            df,
            index=['LOT_WF','ITEM_ID'],
            values='VALUE',
            aggfunc= lambda x: x.mean(),
        ).reset_index()

        res = concat(res, _df, ignore_index=True)

        if 'P15' in option:

            _df = pd.pivot_table(
                df,
                index=['LOT_WF','ITEM_ID'],
                values='VALUE',
                aggfunc= lambda x: x.quantile(0.15),
            ).reset_index()

            res = concat(res, _df, ignore_index=True)

    return df



if __name__ == '__main__':

    option = ['avg', 'med', 'max', 'min', 'P15']


    sp = pd.read_excel(
        r'E:\Codes\sample.xlsx',
        sheet_name='output',
    )

    res = make_aggfunc(sp, option)


    print(res)

    print('End')
