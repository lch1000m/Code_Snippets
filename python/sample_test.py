# test script for partial

from functools import partial


def add(x=1, y=10):
    return x+y


add2 = partial(add, y=2)

result = add2(x=3)

print(result)
