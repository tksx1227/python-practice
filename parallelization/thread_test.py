import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker2(x, y=1):
    logging.debug("start")
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    logging.debug("end")


if __name__ == "__main__":
    # スレッドの名前を name で指定できる
    t1 = threading.Thread(name="rename worker1", target=worker1)
    # 引数を取る関数をスレッドのターゲットにする場合は、タプルと辞書を使い分ける必要がある
    t2 = threading.Thread(target=worker2, args=(100, ), kwargs={"y": 200})
    t1.start()
    t2.start()
    print("started")
