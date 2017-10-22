
import os, psutil, time, sys
from multiprocessing import Process
from pickle_test import save_obj, load_obj


if __name__ == '__main__':

    dic = load_obj('serial.txt')

    pids = []

    for key, val in dic.items():
        pids.append(val)


    while True:
        running_pgms = 0

        for pid in pids:

            try:
                proc = psutil.Process(pid=pid)
                running_pgms += 1
            except:
                pass

        if running_pgms == 0:
            break
        else:
            print('{0} pgms running now!'.format(running_pgms))

        time.sleep(1)

    print('All pgms end! system exit!')
    print('System Shutdown!')

    # os.system('shutdown -s -f -t 5')
