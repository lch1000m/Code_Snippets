
import pandas as pd

import logging


def my_logger():

    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logger = logging.getLogger()

    handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.setLevel(logging.DEBUG)

    return logger



if __name__ == '__main__':

    log = my_logger()

    df = pd.DataFrame({
        'A':[1,2,3],
        'B':[1,2,3],
    })

    assert df.empty, 'df is empty df: {0}'.format(df)

    print(df)
