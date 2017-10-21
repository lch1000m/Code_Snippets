
import multiprocessing
from multiprocessing import Process
import logging
from logging.handlers import QueueHandler, QueueListener
import time
from datetime import datetime as dt


def f(i):
    logging.info('{1} {0} in worker thread start!'.format(i, dt.now()))
    time.sleep(10)
    logging.info('{1} {0} in worker thread End!'.format(i, dt.now()))
    return i


def worker_init(q):
    # all records from worker processes go to qh and then into q
    qh = QueueHandler(q)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(qh)


def logger_init():
    q = multiprocessing.Queue()
    # this is the handler for all log records
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(process)-5s - %(message)s", "%Y-%m-%d %H:%M:%S"))

    # ql gets records from the queue and sends them to the handler
    ql = QueueListener(q, handler)
    ql.start()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # add the handler to the logger so records from this process are handled
    logger.addHandler(handler)

    logger.handlers[0].formatter._fmt = None

    return ql, q


def main():

    q_listener, queue = logger_init()

    logging.info('hello from main thread')

    procs = []

    for i in range(10):
        proc = Process(target=f, args=(q_listener, [queue], i))

        procs.append(proc)

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    q_listener.stop()

if __name__ == '__main__':
    main()