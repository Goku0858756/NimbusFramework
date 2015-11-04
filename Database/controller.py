__author__ = 'N05F3R4TU'


def mongo_start():
    import subprocess
    import shlex
    import os
    from time import sleep
    print("starting server")
    sleep(3)
    # subprocess.call(shlex.split('./server'))
    os.system('./server.sh')

def mongo_stop():
    import subprocess
    import shlex
    from time import sleep
    print("STOPPING server")
    sleep(3)
    subprocess.call(shlex.split('./stop.sh'))

def mongo_pid():
    import subprocess
    import shlex
    print(subprocess.call(shlex.split('cat mongodb.pid')))




if __name__ == '__main__':
    """
        threading via commandline
    """
    from argparse import ArgumentParser
    from threading import Thread
    from queue import Queue

    # parser = ArgumentParser(description="proces description")
    #
    # parser.add_argument("--start", dest="mongo_start", action="store_true")
    # parser.add_argument("--stop", dest="mongo_stop", action="store_true")
    # parser.add_argument("--pid", dest="sum", action="store_true")
    #
    # args = parser.parse_args()
    #
    # print(args)

    try:
        raining = True
        q = Queue()

        while raining:
            command = input("nimbus-input // ")
            if command != "exit":

                if command == "mongostart":
                    msta = Thread(target=mongo_start, args=(), daemon=True)
                    msta.start()
                    continue
                elif command == "mongostop":
                    msto = Thread(target=mongo_stop, args=())
                    msto.start()
                    continue
                elif command == "mongopid":
                    mpid = Thread(target=mongo_pid, args=())
                    mpid.start()
                    continue
                else:
                    print("Command Not Recognised")
                continue

            elif command == "exit":
                raining = False
                print("Goodbye")
            else:
                print("I dont know what you mean")
    except KeyboardInterrupt as e:
        print(" ### Keyboard interruption")

