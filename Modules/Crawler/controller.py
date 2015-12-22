#!/usr/bin/env python
from colorama import Fore, Back, Style, init
from sprint import Sprint

__author__ = 'N05F3R4TU'

init(autoreset=True)
# _MODE = "[ CRAWLER|MODE ]"
#
# def sprint(string, mode=_MODE):
#
#     if mode is None:
#         print("nimbus \> %s" % string)
#     else:
#         print("nimbus " + Back.RED + Fore.GREEN + "{}".format(mode) + Style.RESET_ALL + " \> {}".format(string))



class Arachnida(Sprint):
    """
    Arachnida Mother Crawler Object as Abstract as Possible
    @design-pattern:
    @inherritence:
    @methods: [ ]
    @gets-orders:
    """
    def __init__(self):
        """[ CRAWLER ] Just Crawling Around"""
        import argparse
        super()
        self.modus = "[ CRAWLER|MODE ]"
        self.colors = {"back": Back.RED, "fore": Fore.GREEN}
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "

        self.session_id = id(self)
        self.session_crawl = True


        from Core.banners import Banners
        Banners.arachnida(self)

        self.sprint("ACTIVATED", mode=self.modus)

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework [CRAWLER|MODE ]", description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session_crawl:
            self.command = input(self.session_name)
            if not self.command:
                self.sprint("No Command Given", mode=self.modus)
                continue
            else:
                import re

                if re.match("-", self.command.split()[0]):
                    self.sprint("Wrong! Dont use OPTIONS but choose a COMMAND", mode=self.modus)
                    print(self.usage())
                    continue
                else:
                    self.args = self.parser.parse_args(self.command.split()[0:1])

                    try:
                        if hasattr(self, self.args.command):
                            """ Maybe the Most Important Code of the Whole Framework """
                            getattr(self, self.args.command)()

                        elif not hasattr(self, self.args.command):

                            self.sprint("Unrecognized command", mode=self.modus)
                            self.sprint("try again pall", mode=self.modus)
                            self.sprint("*" * 40 + "\n")
                            print(self.usage(), "\n")
                            self.sprint("*" * 40 + "\n")
                            continue
                        else:
                            print("%s\n%s\n%s" % ("*"*40, "* If you see this message, something went HORRIBLY wrong! Call for help!", "*"*40))
                    except Exception as e:
                        print("[ CRAWLER_EXCEPTION ]", str(e))

    def __str__(self):
        print(self.__dict__)

    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
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
            if attr not in ["usage", "__init__", "__del__", "__str__", "methods", "sprint"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr).__doc__])
        return commands

    def help(self):
        """[ HELP ] For all Options"""
        print(self.usage())

    def crawl(self):
        """[ START ] crawling! """
        from datetime import datetime

        print("Crawler started NOW @ %s" % datetime.now())

    def target(self):
        """[ TARGET ] New Target in Sight"""
        target = Target()

    def set(self):
        self.target

    def leave(self):
        """[ LEAVE ] Mode Gently """
        self.session_crawl = False
        return self


class Target(object):

    def __init__(self, name=None, url=None, ip=None):
        self.id = id(self)
        self.name = name
        self.url = url
        self.ip = ip
        self.decimal = None
        self.sighted = self.target_sighted()

        if self.ip is not None:
            from Plugins.IPConversion import controller
            self.decimal = controller.ip_to_int(self.ip)
            del controller

    def __str__(self):
        return str(self.__dict__)

    def __del__(self):
        print(self.__class__.__name__, "Destructed")

    def target_sighted(self):
        import datetime
        now = datetime.datetime.now()
        return str(now)


# if __name__ == '__main__':
#     t = Target(ip="149.210.192.240")
#     print(t)
#
#     t.name = "QI.NL"
#     t.url = "http://www.qi.nl"
#     # t.ip = "149.210.192.240"
#
#     print(t)
#     print(t.id)
#
