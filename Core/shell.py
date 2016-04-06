from sprint import Sprint
from colorama import Style


class Shell(Sprint):

    def __init__(self):
        import argparse

        self.name = "Shell Object"
        # self.modus = "Shell Mode"
        # self.colors = {"back": Back.LIGHTMAGENTA_EX, "fore": Fore.WHITE}

        self.session_id = id(self)
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "
        self.session = True

        self.sprint("ACTIVATED", mode=self.modus)

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework {}".format(self.modus), description="Need a Description? Really?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session:
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

    def leave(self):
        """[ LEAVE ] Mode Gently """
        self.session = False
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

