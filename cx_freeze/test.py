
import subprocess, os

script_path = r'C:\Codes\Snippets\cx_freeze'

proc = subprocess.Popen(['python','main_script.py'], cwd=script_path)

proc.communicate()
