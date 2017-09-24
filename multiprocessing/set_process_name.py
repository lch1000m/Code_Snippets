# set process name for better understanding

"""
reference
#
"""


import subprocess

executable_code = """

import time

val = 0

while True:
    
    print('value : {0}'.format(val))
    val += 1

    time.sleep(1)

"""

code_with_exception = """
raise Exception()
"""

# ok_rc = subprocess.call(['python', '-c', executable_code])
# assert ok_rc == 0
#
# bad_rc = subprocess.call(['python', '-c', code_with_exception])
# assert bad_rc == 1


exec(executable_code)
