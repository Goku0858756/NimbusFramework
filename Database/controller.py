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
    return

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

def this():
    import os
    print("PID :: ", os.getpid())
    return os.getpid()

def mongo(*args):
    import os
    from time import sleep
    print("Connecting to MongoDB, 1 sec please ..")
    sleep(3)
    os.system("{} {}".format('./server.sh', ' '.join(args[0])))

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
            command = input("nimbus-input // ").split()

            if not command:
                print("Type something in!")
            else:

                if command[0] != "exit":

                    if command[0] == "mongo":
                        msta = Thread(target=mongo_start, args=(), daemon=True)
                        msta.start()

                    elif command[0] == "mongostop":
                        msto = Thread(target=mongo_stop, args=())
                        msto.start()

                    elif command[0] == "mongopid":
                        mpid = Thread(target=mongo_pid, args=())
                        mpid.start()

                    elif command[0] == "pid":
                        pid = Thread(target=this, args=())
                        pid.start()

                    elif command[0] == "db":
                        mongodb = Thread(target=mongo, args=(command[1:],), daemon=True)
                        mongodb.start()

                    else:
                        print("Command Not Recognised")

                elif command[0] == "exit":
                    raining = False
                    print("Goodbye")
                else:
                    print("I dont know what you mean")
            continue

    except KeyboardInterrupt as e:
        print("\n\r\n\r\t### Keyboard interruption\n\r\n\r")

