__author__ = 'N05F3R4TU'
import core
from Modules import controller as mods
from Plugins import controller as plugs
from Database import controller as dbs

# TODO: Nimbus Own Envirement [ @startup ]
# TODO: PID file tracking
# mongod --pidfilepath ~/NimbusFramework/NimbusFramework/Database/dbmongo.pid

# TODO: Create Basic Crawler [√]
# TODO: Create MassScanner
# TODO: Create Plugins
# TODO: Plugins: Gmail [√]
# TODO: Create System [√]
# TODO: System: [ check for ] Update
# TODO: System: Encryption and Decryption
# TODO: Thread Control System
# TODO: CommandLineInterface [√]

# MOST IMPORTANT
# TODO: Threading
# TODO: Services
# TODO: Modules [√]
# TODO: Plugins [√]
# TODO: Body/Framework [√]
# TODO: Documentation System Pythonic

# ------------------

# TODO: IRCBot Refactor Code [√]
# TODO: Subdomain Scanner Import
# TODO: SocksScanner Import
# TODO: Nmap Scanner Import
# TODO: Banner Grabbing Code Refactor

# TODO: Crawler Code Refactor
# TODO: Virtual Env. Auto Deployment

# ------------------

# TODO: OpenSSL implementation
# TODO: OpenVPN implementation



# Design Patterns
# facade system
#



"""
[!] ************************************************************************
[!] *                         COMMAND LiST MODULES                         *
[!] ************************************************************************
[!]
[!] harvest     [DNS, IP range, Emails, Phone-numbers, wp-admins, sub-domains(fierce) ]
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

""" I wanna know the state of the Database"""

class Nimbus(object):
    """
    Nimbus is the Highest Object in the Hierchie in this Framework.
    Nimbus can give Orders through its Framework Object
    Also it is been Inherrited by the Main-Controllers.

    By doing so, Nimbus can be `updated` by its components. Thus it
    can give new orders to its Framework Object
    """

    def __init__(self):
        import os
        self.name = "Nimbus Object"
        self.id = id(self)
        self.thread_id = os.getpid()

    def __str__(self):
        return str(self.__class__.__name__)

    def test_method(self):
        print("This is a test method for inherritence")

def main():
    try:
        app = core.Framework()

    except KeyboardInterrupt as k:
        print("\n\n\t*** [ KEYBOARD INTERRUPT ] ***\n\n")



if __name__ == '__main__':
    from threading import Thread

    # frame = Thread(target=main, args=(), name="AlexAlex", daemon=True)
    # frame.start()
    main()