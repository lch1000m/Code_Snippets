# async file reading using mp

"""
reference
#
"""

import time
import pandas as pd

from multiprocessing import Queue, Process



def q_check_server(q):

    while True:
        print('Current Q Size : {0}'.format(q.qsize()))

        time.sleep(1)


def psuedo_work(q):

    df = q.get()

    print(df)



if __name__ == '__main__':


    q = Queue()  # mp queue for storing segmented df

    proc = Process(target=q_check_server, args=(q,))
    proc.start()



    iter_df = pd.read_csv(
        'sample.txt',
        sep='\t',
        iterator=True,
        chunksize=10,
    )


    q_size_limit = 2

    q_size = 0



    while True:
        for i, df in enumerate(iter_df):
            print('{0}th df processing!'.format(i))

            if q_size < q_size_limit:
                q_size += 1
                q.put(df)
                # pseudo working time
                # psuedo_work(q)
                time.sleep(5)

            else:
                while not q_size < q_size_limit:
                    q_size += 1
                    q.put(df)
                    # pseudo working time
                    # psuedo_work(q)
                    time.sleep(5)


            time.sleep(1)

            time.sleep(0.1)
