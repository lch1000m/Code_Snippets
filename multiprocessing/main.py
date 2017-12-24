
import os, psutil, time, sys

from multiprocessing import Process


if __name__ == '__main__':

    pids = [10340, 2704]

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

    sys.exit(0)
