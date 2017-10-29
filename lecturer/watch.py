import os
import pyinotify
import datetime
from .lecture import CowLecturer

class OpenEventHandler(pyinotify.ProcessEvent):
    def my_init(self, handler):
        self.handler = handler
        self.is_writing = False

    def process_IN_CLOSE_NOWRITE(self, event):
        self.handler(event.pathname)

class Watcher:
    def __init__(self, target_file):
        self.lecturer = CowLecturer()

        if not os.path.isfile(target_file):
            self.lecturer.deliver(target_file)

        wm = pyinotify.WatchManager()
        wm.add_watch(target_file, pyinotify.IN_CLOSE_NOWRITE)

        e = OpenEventHandler(handler=self.lecturer.deliver)
        self.notifier = pyinotify.Notifier(wm, e)

    def run(self):
        self.notifier.loop()
