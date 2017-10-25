
import functools

class Dec(object):

    def __init__(self, name):
        pass

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):

            result = func(*args, **kwargs)

            return result
        return inner




# usage example from here on
@Dec
def example():
    print('example yay')


example()
