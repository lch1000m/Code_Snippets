
import time, os
from pickle_test import save_obj, load_obj

def run_program():
    print('pgm start!')

    time.sleep(60)

    print('pgm end!')



if __name__ == '__main__':

    pid = os.getpid()
    print('pid is {0}'.format(pid))

    dic = load_obj('serial.txt')
    dic.update({'task1':pid})
    save_obj(dic, 'serial.txt')

    run_program()

    dic = load_obj('serial.txt')
    dic.update({'task1': -1})
    save_obj(dic, 'serial.txt')
