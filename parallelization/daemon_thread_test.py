import logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG, format="%(threadName)s: %(message)s")


def worker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def worker2():
    logging.debug("start")
    time.sleep(2)
    logging.debug("end")


if __name__ == "__main__":
    t1 = threading.Thread(target=worker1)
    # デーモン化することで t1 の終了と共に t2 を待たずしてプログラムも終了する
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print("started")
    # ジョインすることで、デーモン化したスレッド以外が終了するまで待つ
    t1.join()
