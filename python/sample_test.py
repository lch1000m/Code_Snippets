# test script for partial

import numpy as np


def round_half_digit(res):

    n, rem = divmod(res, 1)

    if rem >= 0.75:
        res = n + 1
    elif rem >= 0.25:
        res = n + 0.5
    else:
        res = n

    return res



if __name__ == '__main__':

    inp = np.linspace(10, 12, num=11)

    for it in inp:
        res = round_half_digit(it)

        print('{0} - {1}'.format(it, res))
