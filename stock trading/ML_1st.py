# make random forest stock price prediction

import pandas as pd


def main():

    df = pd.read_table(
        r'C:\Codes\Snippets\stock trading\sample.txt',
        index_col=['Date'],
    )

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], iris.target, test_size=0.25)




if __name__ == '__main__':

    main()
