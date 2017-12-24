import time
import os
import shutil
import datetime
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class TestEventHandler(PatternMatchingEventHandler):

    def __init__(self, *args, **kwargs):
        super(TestEventHandler, self).__init__(*args, **kwargs)
        self.last_created = None


    def on_created(self, event):
        path = event.src_path
        if path != self.last_created:
            print(str(datetime.datetime.now()) + " " + str(event))
            self.last_created = path


    def on_deleted(self, event):
        path = event.src_path
        if path == self.last_created:
            self.last_created = None


if __name__ == '__main__':

    path = "C:\\Temp"
    target_dir = "C:\\Temp\\2017\\07\\25"
    src_dir = "C:\\Temp2\\2017\\07\\25"
    filename = 'test.xml'

    target = os.path.join(target_dir, filename)
    src = os.path.join(src_dir, filename)

    event_handler = TestEventHandler(patterns=["*.xml"])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
