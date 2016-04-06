from sprint import Sprint

__author__ = 'N05F3R4TU'


# TODO: Nimbus Own Envirement [ @startup ]
# TODO: PID file tracking
# mongod --pidfilepath ~/NimbusFramework/NimbusFramework/Database/dbmongo.pid

# TODO: Create Basic Crawler [√]
# TODO: Create MassScanner [√]
# TODO: Create Plugins [√]
# TODO: Plugins: Gmail [√]
# TODO: Create System [√]
# TODO: System: [ check for ] Update
# TODO: System: Encryption and Decryption
# TODO: Thread Control System
# TODO: CommandLineInterface [√]

# MOST IMPORTANT
# TODO: Threading [√]
# TODO: Services
# TODO: Modules [√]
# TODO: Plugins [√]
# TODO: Body/Framework [√]
# TODO: Documentation System Pythonic

# ------------------

# TODO: IRCBot Refactor Code [√]
# TODO: Subdomain Scanner Import
# TODO: SocksScanner Import
# TODO: Nmap Scanner Import [√]
# TODO: Banner Grabbing Code Refactor [√]

# TODO: Crawler Code Refactor
# TODO: Virtual Env. Auto Deployment

# ------------------

# TODO: OpenSSL implementation
# TODO: OpenVPN implementation



# facade system




"""
[!] ************************************************************************
[!] *                         COMMAND LiST MODULES                         *
[!] ************************************************************************
[!]
[!] harvest     [DNS, IP range, Emails, Phone-numbers, wp-admins, sub-domains(fierce), NAS,  ]
[!] discover    [frameworks, ]
[!] scan        [port, ip, ]
[!] add         [target, proxy, vpn, chains(strategy),  ]
[!] db          [start, stop, status, pid, kill, ]
[!] job         [jobs, kill, id, ]
[!] system      [encrypt, decrypt, ]
[!] set         []
[!]
[!]
"""




# user = {"username":"tester", "password": "secret"}
#
#
# def logincheck(func):
#
#     def inner(*args, **kwargs):
#         # from Core.banners import Banners
#         # b = Banners()
#         # b.pirate()
#         from Core.banners import Banners as b
#
#         b.pirate()
#
#         print("[!]          AAARRR! Who be traspassin ?")
#         keyword = input("[!]          What be the keyword: ")
#
#         if keyword != user["password"]:
#             print("Invalid")
#         else:
#             print("Password correct!")
#             return func(*args, **kwargs)
#     return inner
#
# # @logincheck
# def services(func):
#     import time
#     """
#         Check Services Before Start
#     """
#
#     def inner(*args, **kwargs):
#         print("Checking If All Services Are Started Before we go on!")
#         time.sleep(2)
#         print("There we Go")
#         time.sleep(1)
#         print("[ Nimbus Database Engine ]")
#         print("[ Nimbus Search Engine Installed ]")
#         print("[ Checking for internet connection ]")
#         print("[ Checking for updates ]")
#
#         print("Lets GO! Hack!@")
#         time.sleep(1)
#
#         return func(args, kwargs)
#     return inner


class Nimbus(Sprint):
    """
    Nimbus is the Highest Object in the Hierchie in this Framework.
    Nimbus can give Orders through its Framework Object
    Also it is been Inherrited by the Main-Controllers.

    By doing so, Nimbus can be `updated` by its components. Thus it
    can give new orders to its Framework Object
    """
    _pinned_target = {}
    _running_services = {}
    _shared_modus = ""
    _shared_targets = []

    """ Target History """
    _last_10_targets = []
    _last_searched = []
    # last pinned target

    # Nimbus Queue Objects [ observer pattern ]
    from queue import Queue
    _queue_crawler  = Queue()
    _queue_target   = Queue()
    _queue_scan     = Queue()
    _queue_xss      = Queue()
    _queue_sqli     = Queue()


    def __init__(self):
        import os
        self.name = "Nimbus Shared Object"
        self.id = id(self)
        self.thread_id = os.getpid()


    def q(self):
        """[ QUEUE ] The Queue Object crawler/target/xss/scan/sqli"""

        try:
            command = self.command.split()[1]
            self.sprint("[!] Queue Object for: {}".format(command))

            queue = ""

            for command in ["crawler", "target", "xss", "scan", "sqli"]:
                try:

                    if command == "crawler":
                        queue = self._queue_crawler
                        break
                    elif command == "target":
                        queue = self._queue_target
                        break
                    elif command == "xss":
                        queue = self._queue_xss
                        break
                    elif command == "scan":
                        queue = self._queue_scan
                        break
                    elif command == "sqli":
                        queue = self._queue_sqli
                        break
                    else:
                        self.sprint("Unknown Queue Command. Try 'q crawler/target/xss/scan/sqli'", mode=self.modus)

                except IndexError as e:
                    self.sprint("[ {} ] {}".format(self.__class__.__name__, str(e)), mode=self.modus)

            self.sprint("--- The Queue is {}empty".format("" if queue.empty() else "NOT "))
            self.sprint("--- The Size of the Queue is currently: {}".format(queue.qsize()))
            self.sprint("--- The Unfninished tasks: {}".format(queue.unfinished_tasks))
            self.sprint("*"*50)
            self.sprint("... ... If you want a more Specific queue of object, then try one of these: 'q crawler/target/xss/scan/sqli'")
        except Exception as e:
            print(Exception("try: 'q ?'"))

    def __str__(self):
        return str(self.__class__.__name__)

    def save(self):
        """[ SAVE ] The State of your session today"""
        print("Save Pinned Target")
        print(self._pinned_target)

        print("Save shared Targets")
        for t in self._shared_targets:
            print(t)

        print("Save Modus")
        print(self._shared_modus)

        print("Save Running Services")
        print(self._running_services)

    def tmux(self):
        """[ TMUX ] Command Line MultiPlexer"""
        import os, sys

        t = self.command.split()[1:]
        # print(" ".join([str(x) for x in t]))
        # " ".join([str(x) for x in t])
        os.system(self.command)


    def help(self):
        """[ HELP ] You can always call for Help"""
        print(self.usage(), "\n")



def main(*args, **kwargs):
    import core

    try:
        # nimbus = Nimbus()
        app = core.Framework()
        # nimbus.attach(app)

    except KeyboardInterrupt:
        print("\n\n\t*** [ KEYBOARD INTERRUPT ] ***\n\n")



if __name__ == '__main__':
    # from threading import Thread
    # frame = Thread(target=main, args=(), name="AlexAlex", daemon=True)
    # frame.start()
    main()