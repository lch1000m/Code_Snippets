
import time
from multiprocessing import Process

from logging.handlers import RotatingFileHandler
import multiprocessing, threading, logging, sys, traceback

class MultiProcessingLog(logging.Handler):

    def __init__(self, filename='test.log'):
        logging.Handler.__init__(self)

        self._handler = RotatingFileHandler(filename)
        self.queue = multiprocessing.Queue(-1)

        t = threading.Thread(target=self.receive)
        t.daemon = True
        t.start()


    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self._handler.setFormatter(fmt)


    def receive(self):
        while True:
            try:
                record = self.queue.get()
                self._handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except:
                traceback.print_exc(file=sys.stderr)


    def send(self, s):
        self.queue.put_nowait(s)


    def _format_record(self, record):
        # ensure that exc_info and args
        # have been stringified.  Removes any chance of
        # unpickleable things inside and possibly reduces
        # message size sent over the pipe
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            dummy = self.format(record)
            record.exc_info = None

        return record


    def emit(self, record):
        try:
            s = self._format_record(record)
            self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


    def close(self):
        self._handler.close()
        logging.Handler.close(self)



def process(num, logger):
    # logger = logging.getLogger(None)

    repeat = 10

    for i in range(num):
        logger.info('{0} response - {1}'.format(num, i))

        time.sleep(1)



if __name__ == '__main__':

    logger = MultiProcessingLog()

    num_process = 5

    for i in range(num_process):
        proc = Process(target=process, args=(i, logger,))

        proc.start()
