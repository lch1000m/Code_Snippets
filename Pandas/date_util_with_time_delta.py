# async file reading using mp

"""
reference
#
"""

from datetime import datetime as dt


def get_time_interval(start, end, **kwargs):
    """
    get time interval(tuple) list from given start & end time

    :param start: start time [datetime.datetime]
    :param end: end time [datetime.datetime]
    :param kwargs: kwargs on relativedelta
    :return: list of time intervals as tuple data types
    """
    from dateutil.relativedelta import relativedelta

    time_interval = []

    end = end + relativedelta(**kwargs)

    res_start = start
    res_end   = None

    count = 0

    while res_start < end:
        if count == 0:  # first tiral
            res_end = res_start + relativedelta(**kwargs)
        else:
            res_end = res_end + relativedelta(**kwargs)

        if res_end > end:   # last time adjust
            res_end = end

        temp = (res_start, res_end)

        time_interval.append(temp)

        count += 1
        res_start = res_end

    return time_interval



if __name__ == '__main__':

    start = dt(2016,  1, 1)
    end   = dt(2017, 11, 1)

    res = get_time_interval(start, end, months=1)

    for i in res:
        print(i)
