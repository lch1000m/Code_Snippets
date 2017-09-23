# make sparse df for memory efficiency

"""
reference
#
"""

import pandas as pd


def num_generate(start, end):

    nums = range(start,end+1)

    res = []

    for num in nums:
        res.append(num)

    return  res



def read_csv_iterator(chunk=50000):

    index = 0

    while True:

        if index == 0:
            _skip = False
        else:
            _skip = num_generate(1, chunk*index)

        # print('index {0}, skip is {1}'.format(index, _skip))

        df = pd.read_csv(
            'sample.txt',
            sep='\t',
            nrows=chunk,
            skiprows=_skip,
        )

        index += 1

        if df.empty:    # df is empty df
            break

        yield df




def main():

    iter_df = read_csv_iterator(chunk=5000)

    for i, df in enumerate(iter_df):
        print('{0}th df processing!'.format(i))

        df['n row'] = df.index + 1

        print(df.head())
        print(df.tail())



if __name__ == '__main__':

    main()
