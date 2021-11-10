import logging
from config_and_logging import logger_test


"""
ログレベルのオーダー
設定したログレベルより下のレベルは表示されない（デフォルトはWARNING）

CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

# # filename を指定すると、ログをファイルに書き出すことができる
# logging.basicConfig(filename="test.log", level=logging.DEBUG)

# formatter を使うとログメッセージをカスタマイズできる
# formatter = "%(levelname)s:%(message)s"
# formatter = "%(asctime)s:%(message)s"
# logging.basicConfig(level=logging.DEBUG, format=formatter)

# logging.critical("critical")
# logging.error("error")
# logging.warning("warning")
# logging.info("info")
# logging.debug("debug")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info("from main")

logger_test.do_something()
