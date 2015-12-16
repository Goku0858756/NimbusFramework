__author__ = 'N05F3R4TU'
from time import sleep
import argparse
from nimbus import Nimbus

def epi():
    print("""

        "He shall be a wild donkey of a man, his hand against everyone and everyone's hand against him,
        and he shall dwell over against all his kinsmen.

                                                                    - Genesis 16:12 -

    """)

def sprint(string):
    print("nimbus \> %s" % string)

class Framework(Nimbus):

    def __init__(self):
        # Shared Target From Nimbus as Mother Object
        print("$$$$$$$$$$$$$$$$$$$$$$$$")
        print(self._pinned_target)
        print("$$$$$$$$$$$$$$$$$$$$$$$$")

        self.session_name = "nimbus \> "
        self.session_state = True
        self.session_id = id(self)
        self.function_name = ""

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework", description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session_state:
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
                            # print("[ HAS ATTRIBUTE ]")
                            getattr(self, self.args.command)()
                            # print("[ AFTER ATTRIBUTE ]")

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
                        print("[ EXCEPTION ]", str(e))



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
            if attr not in ["usage", "__init__", "__del__", "__str__", "methods"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr).__doc__])
        return commands

    def methods(self):
        import inspect
        methods = []
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["__del__", "__str__", "__init__"]:
                methods.append(attr)
        print(methods)


    def crawl(self):
        """[ ARACHNIDA ] Nimbus Calls for Arachnida to Crawl"""
        from Modules.Crawler.controller import Arachnida
        sprint("Calling for Arachnida")

        # from Core.banners import Banners
        # Banners().arachnida()

        crawler = Arachnida()


    def config(self):
        """[ CONFIG ] This option is to configure the framework"""
        print("Config Command")

    def help(self):
        """[ HELP ] Need I say more?"""
        print(self.usage(), "\n")

    def db(self):
        """[ DATABASE ] Control the Database with this option"""
        self.function_name = "db"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Nimbus Loves MongoDB", add_help=True)
        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("--start", dest="start", action="store_true", default=False, help="Start the Database")
                    parser.add_argument("--stop", dest="stop", action="store_true", default=False, help="Stop the Database")
                    parser.add_argument("--status", dest="status", action="store_true", default=False, help="The Status of the Database")
                    parser.add_argument("--add", dest="add", action="store_true", default=False, help="Add something to the database")
                    parser.add_argument("--dbs", dest="dbs", action="store_true", default=False, help="How many databases are there")
                    parser.add_argument("--pid", dest="pid", action="store_true", default=False, help="Database Process ID")
                    parser.add_argument("--use", dest="use", action="store_true", default=False, help="Use Database")

                    # print("[ OPTIONS ]", parser.parse_args(self.command.split()[1:]))
                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Database.controller import DatabaseController
                    DatabaseController(vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break

    def sqli(self):
        """[ SQL INJECTION ] Injection audit"""
        self.function_name = "sqli"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), conflict_handler="resolve", description="Nimbus Rains Acid", add_help=True, epilog=epi())
        # general = parser.add_argument_group("General", description="General Options")
        # misc = parser.add_argument_group("Miscellaneous", description="Misc Options")


        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:

                    # BASIC WHEN in SHELL
                    # -verbose          [-v, -vv]
                    # -background       [--bg]
                    # -give-id          [--id= STRING]
                    # -sessions         [--sessions] {return ALL sessions}
                    # -sessions         { draft | paused | running }
                    # -retrieve-session [--retr= STRING]
                    # -config           { list | new | edit | del }

                    # STANDARD AUTO OPTIONS
                    parser.add_argument("--target", dest="target", action="store", default=None,  help="[ -u ] Example: http://www.site.com/product.php?id=123")
                    parser.add_argument("--optimize-switches", dest="optimize", action="store_true", default=False, help="[ -o ] Optimize switches")
                    parser.add_argument("--all", dest="retrieve", action="store_true", default=False, help="[ --all ] Retrieve everything")
                    parser.add_argument("--wizard", dest="wizard", action="store_true", default=False, help="[ --wizard ] Wizard Mode. Auto-mode")
                    parser.add_argument("--batch", dest="batch", action="store_true", default=False, help="[ --batch ] Never ask for input")

                    # general.add_argument("-u", help="Define a target for me. Example: http://www.site.com/product.php?id=")
                    # misc.add_argument("--wizard", help="Let the Wizard take over")

                    # print("[ OPTIONS ]", parser.parse_args(self.command.split()[1:]))
                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Plugins.SQLmap.controller import SQLIController
                    SQLIController(vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break


    def stats(self):
        """[ STATS ] Get Statistics from the Database"""
        self.function_name = "stats"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Off course We Love Statistics", add_help=True)
        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("--dbs", dest="dbs", action="store_true", default=False, help="What Databases are there in my Database")
                    parser.add_argument("--wp", dest="wp", action="store_true", default=False, help="Statistics about Wordpress")
                    parser.add_argument("--cms", dest="cms", action="store_true", default=False, help="Statistics about All CMS")
                    parser.add_argument("--coll", dest="coll", action="store_true", default=False, help="Show Collections")
                    parser.add_argument("--target", dest="target", action="store_true", default=False, help="Show Targets")
                    parser.add_argument("--proxy", dest="proxy", action="store_true", default=False, help="Show the Available Proxy's")
                    parser.add_argument("--vpn", dest="vpn", action="store_true", default=False, help="Show My VPN's")
                    parser.add_argument("--tasks", dest="tasks", action="store_true", default=False, help="Show my current Tasks")


                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    # from Database.controller import DatabaseController
                    # DatabaseController(vars(args))
                    print("I NEED A STATISTICS OBJECT TO CALL TO")

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break


    def search(self):
        """[ SEARCH ] Engine within Framework"""
        self.function_name = "search"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Nimbus Searches with Thunder", add_help=True)
        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("--start", dest="start", action="store_true", default=False, help="Start the Search Engine")
                    parser.add_argument("--stop", dest="stop", action="store_true", default=False, help="Stop the Search Engine")
                    parser.add_argument("--status", dest="status", action="store_true", default=False, help="The Status of the Search Engine")
                    parser.add_argument("--pid", dest="pid", action="store_true", default=False, help="Search Engine Process ID")

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Dashboard.controller import DashboardController
                    DashboardController("search", vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break

    def target(self):
        """[ TARGET ] Add, Del, Edit targets"""
        from Core.banners import Banners

        self.function_name = "target"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), conflict_handler="resolve",
                                         description=Banners.targets(self))
        process = parser.add_argument_group("  ### Database".upper(), description="{}".format("-"*40))
        shell = parser.add_argument_group("  ### Shell Interactive Mode".upper(), description="{}".format("-"*40))


        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    # Shell Mode
                    shell.add_argument("--shell", dest="shell", action="store_true", default=False, help="Interactive Mode On/Off")

                    # Target Options
                    parser.add_argument("--add", dest="add", action="store", default=None, help="Add a new target to our HitList")
                    parser.add_argument("--edit", dest="edit", action="store_true", default=False, help="Edit the Target")
                    parser.add_argument("--dell", dest="dell", action="store_true", default=False, help="Remove a target from the HitList")
                    parser.add_argument("--pin", dest="pin", action="store", default=None, help="Pin a Target to make it a Victim")
                    parser.add_argument("--pull", dest="pull", action="store_true", default=False, help="Pull the pin from the Victim")

                    # GROUP: Current Targets
                    process.add_argument("--current", action="store_true", default=False, help="Check All current target(s)")

                    # GROUP: Current Running
                    process.add_argument("--running", action="store_true", default=False, help="Check All running processes on target(s)")

                    args = parser.parse_args(self.command.split()[1:])
                    # print(vars(args))

                    if vars(args)['shell']:
                        # First check if SHELL MODE is Activated
                        from Modules.Target.controller import Target
                        shell_mode = Target()
                    else:
                        # If SHell Mode is not Activated, what do you want to do?
                        print("Checking what is all TRUE or FALSE")
                        print(vars(args))

                    """ here we import the method and call the object with our args """
                    # from Plugins.SQLmap.controller import SQLIController
                    # SQLIController(vars(args))
                    print("I NEED A STATISTICS OBJECT TO CALL TO")

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break



    def find(self):
        """[ FIND ] from the Search Engine"""

        # What do you want me to find for you?

        # [ PROTOCOL        ] ([DNS, FTP, FTPS, SSH, SSL, TLS, POP, IMAP, SMTP, SNMP, TELNET, GOPHER, HTTP, NTP/NNTP, HTTPS, UUCP, XMPP, SMB, CWMP])
        """ --prot """

        # [ PACKET          ] ([ICMP, UDP, TCP, IPv4, IPv6, ARP, RARP, DCCP, SCTP])
        """ --pack """

        # [ PORT            ] ([1, 80, 123] OR [21-443])
        """ --port """

        # [ FRAMEWORK       ] ([Wordpress, Joomla, Drupa, Typo3, Magento, OScommerce, Zencart])
        """ --cms """

        # [ LOCATION        ] ({NL:Netherlands, DE:Germany, UK:England, BE:Belgium})
        """ --geo """

        # [ SERVER          ] ([ Apache, IIS, Linux, OSX, IRC, Bitcoin, Gaming, Modem, Router])
        """ --soft """

        # [ OS              ] ([Win XP, Win7, OSX, Linux, Solaris, ... ])
        """ --os """

        # [ VULNERABILITY   ] ([POODLE, XSS, SQL, CSRF, HeartBleed, ])
        """ --vuln """

        # [  STRATEGY       ] (Result of Strategy Scanning)
        """ --str """


        self.function_name = "find"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Nimbus Searches with Thunder", add_help=True)
        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    """
                        Combine Arguments to find What your looking for
                    """
                    parser.add_argument("-s", dest="start", action="store_true", default=False, help="Start the Search Engine")
                    parser.add_argument("--t", dest="stop", action="store_true", default=False, help="Stop the Search Engine")
                    parser.add_argument("--u", dest="status", action="store_true", default=False, help="The Status of the Search Engine")
                    parser.add_argument("--p", dest="pid", action="store_true", default=False, help="Search Engine Process ID")

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Dashboard.controller import DashboardController
                    DashboardController("search", vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break


    def set(self):
        """[ SET ] Every Framework has to have a set function"""
        self.function_name = "set"
        self.set_commands = {}

        parser = argparse.ArgumentParser(prog="Set Function", description="This is a description for the Set function",
                                         usage=self.usage())
        while self.session_state:
            if not self.command.split()[1:]:
                break
            elif self.command.split()[1:]:
                try:
                    parser.add_argument("-?", dest="?")
                    parser.add_argument("-n", "--name", dest="set_name")
                except Exception as e:
                    raise Exception("[ SET ]", str(e))
                args = parser.parse_args(self.command.split()[1:])

    def add(self):
        """[ ADD ] Proxy, VPN, Task, Strategy, Targets, Rules to the Database"""

        self.function_name = "add"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Nimbus Love to receive water", add_help=True)
        while self.session_state:
            try:
                if not self.command.split()[1:]:
                    sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("--vpn", dest="vpn", action="store_true", default=False, help="Add VPN information")
                    parser.add_argument("--proxy", dest="proxy", action="store_true", default=False, help="Add PROXY information")
                    parser.add_argument("--target", dest="target", action="store_true", default=False, help="Add potential Targets")
                    parser.add_argument("--strategy", dest="strategy", action="store_true", default=False, help="Add a Strategy to the Database")
                    parser.add_argument("--rule", dest="rule", action="store_true", default=False, help="Add a Rule to the Database")
                    parser.add_argument("--task", dest="task", action="store_true", default=False, help="Add a Task into the Queue")

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Dashboard.controller import DashboardController
                    DashboardController("search", vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break

    def service(self):
        """[ SERVICES ] What services are running at this moment"""
        self.function_name = "service"
        print('''
        + ---------------- +
        | service  | UP    |
        + ---------------- +
        | service  | DOWN  |
        + ---------------- +
        ''')


    def exit(self):
        """[ QUIT ] To quit the Framework type `exit`"""
        self.session_state = False
        sprint("[!] ************************************************************************")
        sprint("[!] *       Here and Now i want to take a moment to thank a special        *")
        sprint("[!] *               friend of my who moved away to Canada                  *")
        sprint("[!] *          He helped me on my way at school, hacking, programming      *")
        sprint("[!] *                     and life. I'll miss you!                         *")
        sprint("[!] *                                                                      *")
        sprint("[!] *                          - Thanx Buddy --                            *")
        sprint("[!] *                                                                      *")
        sprint("[!] *              Please use Numbis Framework with care ;)                *")
        sprint("[!] *  Details: https://github.com/....../nimbus-framework/pull/####       *")
        sprint("[!] ************************************************************************")
        sprint("[!]                                       Rain with Rage, Exploit with Love ")
