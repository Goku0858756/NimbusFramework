__author__ = 'N05F3R4TU'
import core

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




user = {"username":"tester", "password": "secret"}


def logincheck(func):

    def inner(*args, **kwargs):
        from Core.banners import Banners
        b = Banners()
        b.pirate()

        print("[!]          AAARRR! Who be traspassin ?")
        keyword = input("[!]          What be the keyword: ")

        if keyword != user["password"]:
            print("Invalid")
        else:
            print("Password correct!")
            return func(*args, **kwargs)
    return inner


def services(func):
    import time
    """
        Check Services Before Start
    """

    def inner(*args, **kwargs):
        print("Checking If All Services Are Started Before we go on!")
        time.sleep(2)
        print("There we Go")
        time.sleep(1)
        print("[ Nimbus Database Engine ]")
        print("[ Nimbus Search Engine Installed ]")
        print("[ Checking for internet connection ]")
        print("[ Checking for updates ]")

        print("Lets GO! Hack!@")
        time.sleep(1)

        return func(args, kwargs)
    return inner


class Nimbus(object):
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

    def __init__(self):
        import os
        self.name = "Nimbus Shared Object"
        self.id = id(self)
        self.thread_id = os.getpid()

    def __str__(self):
        return str(self.__class__.__name__)

    def __test_method(self):
        print("This is a test method for inherritence")




@services
def main(*args, **kwargs):
    try:
        app = core.Framework()
    except KeyboardInterrupt as k:
        print("\n\n\t*** [ KEYBOARD INTERRUPT ] ***\n\n")



if __name__ == '__main__':
    from threading import Thread

    # frame = Thread(target=main, args=(), name="AlexAlex", daemon=True)
    # frame.start()
    main()