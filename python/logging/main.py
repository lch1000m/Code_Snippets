
import logging
from sub_mod import my_func

logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger()

handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.setLevel(logging.DEBUG)


if __name__ == '__main__':

    logger.info('Main Start!')

    my_func()

    logger.info('Main End!')
