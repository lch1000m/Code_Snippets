
import subprocess

proc = subprocess.Popen(['python','C:\Codes\Snippets\psutil\shutdown_setpoint.py'], subprocess.CREATE_NEW_CONSOLE, shell=True)

proc.communicate()
