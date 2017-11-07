
import time

def yld(iterable):

    for i in iterable:
        yield i



if __name__ == '__main__':

    inp = [1,2,3,4,5]

    iter = yld(inp)

    while True:
        try:
            print(next(iter))
        except:
            break

        time.sleep(1)
