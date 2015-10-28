__author__ = 'N05F3R4TU'
from time import sleep
from asyncio import BaseEventLoop
from asyncio_mongo import 

def start():
    """
    Start Framework aSyncio
    :return:
    """
    state = True
    num = 0

    while state:
        num += 1
        print(num)
        sleep(10)




if __name__ == '__main__':


    try:
        start = True
        while start:
            command = input("your-input // ")

            if command != "exit":

                if command == "start":
                    BaseEventLoop.run_forever()

            else:
                start = False
    except KeyboardInterrupt as e:
        print("\n\n\r\t*** Keyboard Intererruption ***\n\r")
