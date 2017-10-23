
import subprocess, time

from multiprocessing import Process
from sub_func import sub_server


def main():

    while True:
        print('main server work!')

        time.sleep(1)


if __name__ == '__main__':

    proc = Process(target=main)
    proc.start()

    subprocess.Popen(
        [
            'python',
            r'C:\Codes\Snippets\task_batch_code\subprocess popen server\sub_func.py',
        ]
    )
