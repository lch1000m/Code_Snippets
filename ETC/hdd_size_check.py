
import shutil

res = shutil.disk_usage(r'D:')

print(res[0]/1024/1024/1024/1024)
