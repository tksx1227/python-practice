import logging


"""
ログレベルのオーダー
設定したログレベルより下のレベルは表示されない（デフォルトはWARNING）

CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

# filename を指定すると、ログをファイルに書き出すことができる
logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
