
import time, ctypes


input_val = 5


res = ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

if res == 1:

    for i in range(input_val):
        print('{0}th repeat!'.format(i))

        time.sleep(1)
