__author__ = 'N05F3R4TU'
from colorama import Fore, Back, Style, init
init(autoreset=True)

# def sprint(string):
#     print("nimbus \> %s" % string)


class Sprint(object):

    def __init__(self):
        self.name = "String Special print Object"
        self.colors = {"back": Back.RED, "fore": Fore.GREEN}
        self.modus = ""
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "


    def sprint(self, string, mode=None):

        if mode is None:
            print("nimbus \> %s" % string)
        else:
            print("nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> {}".format(string))