
import logging, time

logger = logging.getLogger(__name__)


def my_func():

    logger.debug('sub module Start!')

    time.sleep(2)

    logger.debug('sub module End!')
