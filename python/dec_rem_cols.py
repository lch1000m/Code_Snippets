
import pandas as pd


def remove_dup_cols(func):
    def inner(*args, **kwargs):

        init = args[0].shape

        result = func(*args, **kwargs)

        for col in result.columns:
            if '_rem' in col:
                del result[col]

        end = result.shape

        print('column change : {0}'.format(end[1] - init[1]))
        print('rows change : {0}'.format(end[0] - init[0]))

        return result

    return inner



def read_df():
    df1 = pd.read_excel(
        r'C:\Codes\Snippets\sample data\sample.xlsx',
        sheetname='a',
    )

    return df1


@remove_dup_cols
def rem_cols(df):
    return df

# df2 = pd.read_excel(
#     r'C:\Codes\Snippets\sample data\sample.xlsx',
#     sheetname='b',
# )

if __name__ == '__main__':

    df1 = read_df()
    df1 = rem_cols(df1)

    print(df1)

    import pdb; pdb.set_trace()
