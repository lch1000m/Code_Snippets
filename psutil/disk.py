
import psutil

# # disk usage
# path = 'C:'
# res = psutil.disk_usage(path)


# # memory usage
# res = psutil.swap_memory()


res = psutil.process_iter()


for proc in res:
    if 'chrome' in proc.name():
        print(proc)

# print(res)
