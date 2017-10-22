
import time, os

def run_program():
    print('pgm start!')

    time.sleep(30)

    print('pgm end!')



if __name__ == '__main__':

    print('pid is {0}'.format(os.getpid()))

    run_program()
