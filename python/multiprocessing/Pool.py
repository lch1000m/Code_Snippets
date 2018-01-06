
"""
reference
# http://hamait.tistory.com/755
"""

from multiprocessing import Pool
from datetime import datetime as dt


def doubler(n):
    return n**2



if __name__ == '__main__':

    cpu_counts = range(16)

    repeat = 10000000

    numbers = range(repeat)


    for cpu in cpu_counts :
        _cpu = cpu + 1

        _start = dt.now()

        pool = Pool(processes=_cpu)

        res = pool.map(doubler, numbers)

        _end = dt.now()

        print('{0} Total Time : {1}'.format(_cpu, _end-_start))
