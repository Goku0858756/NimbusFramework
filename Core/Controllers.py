__author__ = 'N05F3R4TU'
from threading import Thread
from queue import Queue
# from time import sleep
import time
import multiprocessing

COUNT = 0


def werkgever(num, q):

    while num > 0:
        q.put(num)
        time.sleep(2)
        num -= 1
    q.put(None)


def aannemer(q):

    while True:
        item = q.get()
        if item is None:
            break
        print("Nieuw Contract num:", item)
    print("Alles Klaar")





def high(q):
    for c in range(0, 9099):
        q.put(c)
    q.put(None)


def low(q):
    count = 1
    start_time = time.time()

    while True:

        item = q.get()
        if item is None:
            break

        fibonacci(count, item)
        count += 1

    end_time = time.time()

    print("Done Completely")
    timer = end_time - start_time
    print(timer)



def fibonacci(count, n):

    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return print(count, " ###### ", a)


# for c in range(0, 9000):
#     print(fibonacci(c))


def scraper():
    import requests

    u = ['http://www.bol.com', 'http://www.nu.nl', 'http://www.sunweb.nl', 'http://www.nos.nl', 'http://www.stackoverflow.com']
    for i in u:
        req = requests.get(url=i)
        print(req.text)

    time.sleep(5)
    for i in u:
        req = requests.get(url=i)
        print(req.text)


if __name__ == '__main__':
    # q = Queue()
    # werk = Thread(target=werkgever, args=(10, q))
    # werk.start()
    # vaklui = Thread(target=aannemer, args=(q,))
    # vaklui.start()
    # vaklui.join()
    #
    # q = multiprocessing.Queue()
    #
    # werk = multiprocessing.Process(target=werkgever, args=(10, q))
    # werk.start()
    # vaklui = multiprocessing.Process(target=aannemer, args=(q,))
    # vaklui.start()
    # vaklui.join()
    #
    # q = multiprocessing.Queue()
    #
    # h = multiprocessing.Process(target=high, args=(q,))
    # h.start()
    #
    # r = multiprocessing.Process(target=scraper, args=())
    # r.start()
    #
    # l = multiprocessing.Process(target=low, args=(q,))
    # l.start()
    # print(l.pid)
    # print(l.is_alive())
    # l.join()

    try:
        q = Queue()
        h = Thread(target=high, args=(q,))
        h.start()

        l = Thread(target=scraper, args=(), daemon=True)
        l.start()

        r = Thread(target=low, args=(q,))
        r.start()
    except KeyboardInterrupt as e:
        print("\n\n\r\t *** KEYBOARD INTERRUPED ***\n\n")

