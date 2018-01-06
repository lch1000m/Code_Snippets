import logging
import multiprocessing
import time

import mplog_source

FORMAT = '%(asctime)s - %(processName)-15s - %(levelname)-10s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
existing_logger = logging.getLogger('x')

logger = logging.getLogger()
hdlr = logging.FileHandler('sample.log')
formatter = logging.Formatter(FORMAT)
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)


def subprocess(n):
    existing_logger.info('y')
    logger = logging.getLogger('sub')
    logger.info('Before sleep.')
    time.sleep(10)
    logger.info('After sleep.')

    root = logging.getLogger()
    root.debug('Root log message.')


def subprocess2(n):
    existing_logger.info('y')
    logger = logging.getLogger('sub')
    logger.info('Before sleep.')
    time.sleep(3)
    logger.info('After sleep.')

    root = logging.getLogger()
    root.debug('Root log message.')


def start_processes(log_queue):file_source
    procs = list()
    for i in range(5):
        proc = multiprocessing.Process(
            target=mplog_source.logged_call,
            args=(log_queue, subprocess, i)
        )

        proc2 = multiprocessing.Process(
            target=mplog_source.logged_call,
            args=(log_queue, subprocess2, i)
        )

        proc.start()
        proc2.start()
        procs.append(proc)
        procs.append(proc2)

    for proc in procs:
        proc.join()


def main():
    existing_logger.info('Before')

    with mplog_source.open_queue() as log_queue:
        existing_logger.info('In context manager.')
        start_processes(log_queue)
        existing_logger.info('At the end.')

    logging.info('Now really quitting.')


if __name__ == '__main__':
    main()
