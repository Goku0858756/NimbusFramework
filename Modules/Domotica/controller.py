from colorama import Fore, Back, Style, init
from nimbus import Nimbus
from Core.shell import Shell


class DomoticaShell(Shell, Nimbus):

    def __init__(self):

        self.name = "Domotica Controller Object"
        self.modus = "[ DOMOTICA|MODE ]"
        self.colors = {"back": Back.LIGHTMAGENTA_EX, "fore": Fore.WHITE}

        # Initiate Shell
        super().__init__()


    def lights(self):
        """[ HUE ] Domotica Lighting Control"""

        print(self.command)

        """
        lights get
                   group

        lights set
                   group
        """

    def doorbell(self):
        pass

    def door(self):
        pass



# if __name__ == '__main__':
#     d = DomoticaShell()