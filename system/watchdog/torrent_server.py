# torrent server program

# reference :
# https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes

import time, os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        file = event.src_path

        try:
            if '.torrent' in file:
                # run file
                os.startfile(file)
                # remove file
                time.sleep(5)
                os.remove(file)

                print('{0} torrent added!'.format(file))

        except:
            pass


if __name__ == "__main__":

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=r'D:\ChangHyung\영화\무라이\download', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
