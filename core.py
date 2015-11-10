__author__ = 'N05F3R4TU'
from time import sleep
import argparse, os


def sprint(string):
    print("nimbus \> %s" % string)

class Framework(object):

    def __init__(self):

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
        """Nimbus Calls for Arachnida to Crawl"""
        from Modules.Crawler.controller import Arachnida


    def config(self):
        """This option is to configure the framework"""
        print("Config Command")

    def db(self):
        """[ Database ] Control the Database with this option"""
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

                    # print("[ OPTIONS ]", parser.parse_args(self.command.split()[1:]))
                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Database.controller import DatabaseController
                    DatabaseController(vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break


    def stats(self):
        """Get Statistics from the Database"""
        self.function_name = "stats"
        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Off course We Love Statistics", add_help=True)
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

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Database.controller import DatabaseController
                    DatabaseController(vars(args))

            except Exception as e:
                sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break


    def set(self):
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
        """Add [ VPN, Proxy, Job, Template, Targets ] in the Database"""
        pass

    def service(self):
        """What services are running at this moment"""
        self.function_name = "service"
        service_parser = argparse.ArgumentParser(prog="Set Function", description="This is a description for the Set function")

        while self.session_state:
            if not self.command.split()[1:]:
                sprint("You didnt give me any [OPTIONS]")
                sleep(2)
                break
            elif self.command.split()[1:]:
                try:
                    service_parser.add_argument("--up", dest="up")
                    service_parser.add_argument("--all", dest="all")
                    service_parser.add_argument("--mongo", dest="mongo")
                except Exception as e:
                    raise Exception("[ SERVICE ]", str(e))
                args = service_parser.parse_args(self.command.split()[1:])
                break

    def exit(self):
        """To quit the Framework type `exit`"""
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
