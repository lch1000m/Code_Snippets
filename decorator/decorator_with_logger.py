
import functools, logging

class Named_Logger(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):

            result = func(*args, **kwargs)

            return result
        return inner


Named_Logger2 = Named_Logger('task1')


# usage example from here on
@Named_Logger2
def example():
    print('example yay')


example()
