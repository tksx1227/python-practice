import logging


# モジュールごとにロガーを作成してカスタマイズすることが一般的
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def do_something():
    logger.info("from logger_test")
    logger.debug("from logger_test_debug")
