
import subprocess

procs = []

for i in range(5):

    proc = subprocess.Popen(['python','sub_process.py','-i',str(i)])
    procs.append(proc)


for proc in procs:
    proc.communicate()
