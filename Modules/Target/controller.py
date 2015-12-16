#!/usr/bin/env python
from colorama import Fore, Back, Style, init
from time import sleep
from nimbus import Nimbus

__author__ = 'N05F3R4TU'
__version__ = "2.1"
__license__ = "Nimbus Corp"

init(autoreset=True)
_MODE = "[ TARGET|MODE ]"

def sprint(string, mode=_MODE):

    if mode is None:
        print("nimbus \> %s" % string)
    else:
        print("nimbus " + Back.BLUE + Fore.YELLOW + "{}".format(mode) + Style.RESET_ALL + " \> {}".format(string))


class Target(Nimbus):

    def __init__(self):
        """[ TARGET ] Looking for VICTIMS"""


        import argparse
        self.session_name = "nimbus " + Back.BLUE + Fore.YELLOW + "{}".format(_MODE) + Style.RESET_ALL + " \> "
        self.session_id = id(self)
        self.session = True

        sprint("ACTIVATED")

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework [CRAWLER|MODE ]", description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session:
            self.command = input(self.session_name)
            if not self.command:
                sprint("No Command Given")
                continue
            else:
                import re

                if re.match("-", self.command.split()[0]):
                    sprint("Wrong! Dont use OPTIONS but choose a COMMAND")
                    print(self.usage())
                    continue
                else:
                    self.args = self.parser.parse_args(self.command.split()[0:1])

                    try:
                        if hasattr(self, self.args.command):
                            """ Maybe the Most Important Code of the Whole Framework """
                            getattr(self, self.args.command)()

                        elif not hasattr(self, self.args.command):

                            sprint("Unrecognized command")
                            sprint("try again pall")
                            sleep(1)
                            sprint("*" * 40 + "\n")
                            print(self.usage(), "\n")
                            sprint("*" * 40 + "\n")
                            continue
                        else:
                            print("%s\n%s\n%s" % ("*"*40, "* If you see this message, something went HORRIBLY wrong! Call for help!", "*"*40))
                    except Exception as e:
                        print(str("[ {}_EXCEPTION ]".format(self.__class__.name)).upper(), str(e))



    def __str__(self):
        sprint(self.__dict__)

    def __del__(self):
        sprint(self.__class__.__name__, "Destroyed")
        return self

    def usage(self):
        """Usage Coomment String"""
        import inspect
        from Core.banners import Banners
        from veryprettytable import VeryPrettyTable
        banner = Banners()

        commands = VeryPrettyTable(["Command", "Description"])
        commands.align = "l"
        commands.padding_width = 2

        banner.randomize()
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["usage", "__init__", "__del__", "__str__", "methods"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr).__doc__])
        return commands

    # def add(self):
    #     """[ ADD ] New Victim to attack"""
    #
    #     target = TargetAdd() # Target Template dict() instantiated
    #
    #     add = True
    #     add_by_list = {"4":"URL".upper(), "3":"Name".upper(), "2":"IP".upper(), "1":"Contract".upper()}
    #
    #     print("\n## Add new Target By:")
    #     for k, v in add_by_list.items():
    #         print("## %s %s" % (k, v))
    #     while add:
    #         add_by = input("## Input [1, 2 or 3]: ".format("-"*40))
    #         if add_by not in add_by_list.keys():
    #             print("This is not a correct number. Try again!")
    #             continue
    #         else:
    #
    #             if add_by_list["{}".format(add_by)] == "name".upper():
    #                 target_name = input("Give me a Target Name: ")
    #                 self._pinned_target.update({"target": target_name})
    #                 print(target)
    #
    #             elif add_by_list["{}".format(add_by)] == "ip".upper():
    #                 print("## Multiple IPs possible by a comma sepperation. E.g; 1.2.3.4, 8.8.8.8, ... ")
    #                 target_ip = input("Can I have the IP(s) please? ")
    #                 print(target_ip.split(",")[:])
    #
    #             elif add_by_list["{}".format(add_by)] == "template".upper():
    #                 print("Load a .temp file into the Framework")
    #
    #             elif add_by_list["{}".format(add_by)] == "URL".upper():
    #                 print("## Multiple URLs possible by a comma sepperation. E.g; http://www.mysite.com, http://www.target.com, ... ")
    #                 target_url = input("URLs to check? ")
    #                 print(target_url.split(",")[:])
    #                 for u in target_url.split(",")[:]:
    #                     print(u.strip())
    #
    #             break
    #
    #
    #     #     # Update Shared/Pinned Object. First Ask
    #     #     self._pinned_target.update({"target_name": add_by_name})
    #     #
    #     #     from pymongo import MongoClient
    #     #     from pymongo.errors import ConnectionFailure
    #     #     import sys
    #     #
    #     #     try:
    #     #         conn = MongoClient(host="localhost", port=27017)
    #     #     except ConnectionFailure as e:
    #     #         sys.stderr.write("Could not connect to MongoDB: %s" % e)
    #     #         sys.exit(1)
    #     #     else:
    #     #         db = conn["targets"]
    #     #         db["target"].insert_one({"target_name": add_by_name})
    #     #     finally:
    #     #         conn.close()
    #     #     break

    def help(self):
        """[ HELP ] For all Options"""
        print(self.usage())

    def rem(self, name):
        """[ REM ] Remove from Hitlist"""
        print("Remove a Target from the Hitlist")
        self._pinned_target.pop(key=name)
        print("succes POPPED key")

    def edit(self):
        """[ EDIT ] Edit my a Target"""

    def list(self):
        """[ LIST ] My Current Victim List"""
        sprint("My current Hitlist")
        print(self._pinned_target)

    def active(self):
        """[ ACTIVE ] The poor Bastards, They will never see me coming"""
        sprint("Victim which are being attacked")

    def leave(self):
        """[ LEAVE ] Mode Gently"""
        self.session = False
        return self

    def add(self):
        """[ ADD ] New Victim to attack"""
        import argparse

        self.function_name = "add"
        session_target_add = True

        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Their surrender is inevitable", add_help=True)

        while session_target_add:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("-n", dest="name", action="store", default=None, help="Add target into system by Name")
                    parser.add_argument("-c", dest="contract", action="store", default=None, help="Add target by contract")
                    parser.add_argument("-i", dest="ip", action="store", default=None, help="Add target by IP")
                    parser.add_argument("-u", dest="url", action="store", default=None, help="Add target by URL. E.g: http://www.victim.com")
                    parser.add_argument("-t", dest="template", action="store_true", default=False, help="Add target by complete Template")

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    target = TargetAdd() # Instantiate Target Object
                    print(target)

                    if args.template:
                        print(">>> By Template")
                    else:
                        if args.name != None:
                            target.target_name = args.name
                        elif args.contract != None:
                            target.target_contract = target.contract
                        elif args.ip != None:
                            target.target_ip = args.ip
                        elif args.url != None:
                            target.target_url = args.url

                    self._pinned_target.update(vars(target))


            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break

class TargetAdd(object):

    def __init__(self):
        import datetime
        self.target_id = None

        self.target_contract = None
        self.target_name = None
        self.target_ip = []
        self.target_url = []

        self.target_dns = []
        self.target_desc = None
        self.target_email = []
        self.target_ports = None
        self.target_scans = []
        self.target_time = str(datetime.datetime.now())

    def __str__(self):
        return str(self.__dict__)
#
#
# if __name__ == '__main__':
#     s = {
#         "_id": ObjectId("234534534545"),
#
#         "_name": "target_name"
#         "_ip": [],
#         "_website": "http://www.bol.com",
#         "_contract": "QI.HC.1000234",
#
#         "_description": "",
#         "_timestamp": date.now(),
#         "_scanned": True/False
#
#         "ports": {
#         }
#
#         "dns": {
#         }
#
#         "xss": {
#         }
#
#         "sql": {
#         }
#
#         "harvest": {
#         }
#
#         "banner": base64("egffdg345t345terff"),
#
#     }