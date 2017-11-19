
import time, subprocess

from sub_func import sub

while True:

    # subprocess.Popen(['python', 'sub_func.py'])
    sub()

    time.sleep(5)
