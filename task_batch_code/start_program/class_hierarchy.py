
from multiprocessing import Process


class Process():

    def __init__(self, name, method='other'):
        self.name = name
        self.method = method


    def __call__(self):
        if self.method == 'inner':
            pass
