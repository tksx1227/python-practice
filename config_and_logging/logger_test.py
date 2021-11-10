import logging


# モジュールごとにロガーを作成してカスタマイズすることが一般的
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ハンドラーを作成することで、ロガーのメッセージを任意の場所に書き出せる
h = logging.FileHandler("logtest.log")
logger.addHandler(h)


def do_something():
    logger.info("from logger_test")
    logger.debug("from logger_test_debug")
