__author__ = 'N05F3R4TU'
from nimbus import Nimbus
from sprint import Sprint
from colorama import Fore, Back, Style, init
import argparse

__all__ = ["Scanner", "ScannerShell"]

class Scanner(Nimbus, Sprint):
    """
    Abstract Scanner Object
    Calling to Child Objects to do Jobs
    @Scans to MongoDB with base64
    """
    def __init__(self, ip=None):
        super(Scanner, self).__init__()
        self.name = "Scanner Concrete Object"
        self.ip = ip


    def port(self):
        """[ NMAP ] Nmap port Scan """
        """
            Open new window -n scan-ip_to_dec
            with arguments

        """
        pass

    def subdomain(self):
        """[ SUB. ] KnockPy """
        """
            Open new-window -n scan-subdom-ip_to_dec
        """
        pass

    def vhost(self):
        """[ vHost ] Scan for possible domain neighbours"""
        pass

    def socket(self):
        """[ PROXY ] SockScan for Proxy """
        pass

    def wp(self):
        """[ WORDPRESS ] Wordpress Scan """
        pass

    def nslookup(self):
        """[ REVERSE ] Do a NSLookup """
        pass

    def whois(self):
        """[ WHOIS ] Do a whois lookup """
        pass

    def webserver(self):
        """[ SERVER ] Determine if there is a webserver living on the host """
        pass
        # nmap -Pn -p80 -oX logs/pb-port80scan.xml -oG logs/pb-port80scan.gnmap 216.163.128.20/20

    def xss(self):
        """[ XSS ] Scan for possible Cross-Site Scripting vulnerabilities"""
        pass

    def dns(self):
        """[ DNS ] Scan for possible DNS attacks"""
        pass

    def sql(self):
        """[ SQL ] Scan for possible SQL Injections"""
        pass

    def cms(self):
        """[ CMS ] Scan target for possible CMS recognition"""
        pass


class ScannerShell(Scanner):

    def __init__(self):
        """
        Scanner Shell Mode
        :return:
        """
        super(ScannerShell, self).__init__(self)
        self.name = "Scanner Shell Mode Object"
        self.modus = "[ SCANNER|MODE ]"
        self.colors = {"back": Back.YELLOW, "fore": Fore.BLUE}

        self.session_id = id(self)
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "
        self.session_scan = True

        self.sprint("Scanner Shell Activated", mode=self.modus)

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework {}".format(self.modus), description="The search has already been started !", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session_scan:
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
                elif self.command.split()[0] == "?":
                    print(self.usage())
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
                        print(str("[ {}_EXCEPTION ]".format(self.__class__.__name__)).upper(), str(e))

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

    def leave(self):
        """[ LEAVE ] This mode Gently"""
        self.session_scan = False
