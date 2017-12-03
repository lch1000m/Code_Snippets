
import psutil, time

time_interval = 5

def setpoint_killer():

    res = 'Not Done'
    for proc in psutil.process_iter():
        try:
            if proc.cmdline() == ['C:\\Program Files\\Logitech\\SetPointP\\SetPoint.exe', '/launchGaming']:
                proc.kill()
                print('Setpoint Process killed!')
                res = 'Done'
        except:
            pass

    return res


while True:

    res = setpoint_killer()

    if res == 'Done':
        break
    else:
        time.sleep(5)
