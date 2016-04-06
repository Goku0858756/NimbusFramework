#!/usr/bin/env python
from colorama import Fore, Back, Style, init
from pymongo import MongoClient
from Modules.Target.controller import TargetFunctions
from nimbus import Nimbus
from sprint import Sprint

from Plugins.NimbusCrawler.spider import Spider
from threading import Thread

mongo = MongoClient('localhost', port=27017, connect=True)
db = mongo["targets"]["targets"]

__author__ = 'N05F3R4TU'

init(autoreset=True)


def crawl_usage():
    import subprocess, os

    # subprocess.call("./crawl_usage.sh", shell=True)
    full_path = os.path.dirname(os.path.realpath(__file__))
    os.system("cat {}/{}".format(full_path, "crawl_usage.sh"))



class CrawlerFunctions:

    def __init__(self):
        self.name = "Crawler Functions Object"
        self.command = ""
        self.modus = ""

    def worker(self):
        """ THREAD - WerkNemer"""
        pass

    def crawl(self):
        """ Spider Boss Arachnida - WerkGever """
        pass

    def stop(self):
        print("Stop with crawling")
    def pause(self):
        print("Pause Crawler")
    def start(self):
        print("Start/Resume Crawling")

    def discover(self):
        """[ DISCOVER ] cms, framework, specific HTML5 stuff"""

        """
            IF input_parameter == cms:
                then; Discover if TARGET is a type of CMS
            IF input_parameter == framework
                then; DISCOVER if TARGET is a using a type of FRAMEWORK
        """
        pass

    # def crawl(self):
    #     """[ START ] crawling the pinned Target! 'crawl help' for more info"""
    #
    #     import re
    #
    #     # crawl [commands]:[value]
    #     crawler_help = ["help", "?", "-h", "--help"]
    #     crawler_commands = ["url", "name", "id", "ip", "pinned", "file", "config"]
    #
    #     try:
    #         # check of er iets is ingevuld
    #         if len(self.command.split()[1:]) >= 1:
    #
    #             # er is iets gevuld
    #             # is het een commando zonder value of een Key:Value
    #             for i in self.command.split()[1:]:
    #
    #                 # check if command has arguments crawl key but no :Value
    #                 if re.search(":", i):
    #
    #                     # split every argument in Key and Value
    #                     k, v = i.split(":", 1)[0], i.split(":", 1)[1]
    #
    #                     # check if key is in commands
    #                     if k in crawler_commands and v != "":
    #                         print("The command is {}".format(k))
    #                         print("The value what was given is: {}".format(v))
    #
    #                         try:
    #                             """ Start devision """
    #                             # if key is url
    #                             if k == "url":
    #
    #                                 # check in database if url is known
    #                                 found = db.find({"target_{}".format(k):v})
    #
    #                                 # print length of found
    #                                 print(found.count())
    #
    #                                 if found.count() == 0:
    #                                     self.sprint("[!] This URL is not found in the database", mode=self.modus)
    #                                     add_url = input("[?] Do you want to add this URL to the database? Y/n ").lower()
    #
    #                                     while True:
    #                                         if add_url == "Y".lower() or add_url == "Yes".lower():
    #                                             self.sprint("Create a new Target Model Object and pus it into the Database")
    #                                             from Modules.Target.models import AddTarget
    #                                             target = AddTarget(url=v)
    #                                             db.insert_one(target.__dict__)
    #                                             break
    #                                         elif add_url == "n".lower() or add_url == "no".lower():
    #                                             self.sprint("No? Then we will proceed without the Database ;)", mode=self.modus)
    #                                             break
    #                                         else:
    #                                             print("Try again!")
    #                                             continue
    #
    #
    #
    #                                     """ Hier gebleven """
    #
    #                                 elif found.count() == 1:
    #
    #                                     # just found 1 target record
    #                                     # therefor we can proceed with this target
    #                                     print("found just 1 record")
    #                                     print("return a table with this records")
    #                                     print("is this correct? shall we proceed? Y/n ")
    #                                     break
    #                                 else:
    #                                     # found multiple records
    #                                     # loop over the found records
    #                                     for url in found:
    #                                         print(url)
    #
    #                                 continue
    #
    #                             elif k in ["name", "id", "pinned", "ip"]:
    #
    #                                 # check in database if target is known
    #
    #                                     # if yes, check for target_url to crawl
    #                                     # if no
    #                                         # print Err. No such target_{{ key }}
    #                                         # do you want to save this target and append more info?
    #                                 continue
    #                             elif k in ["file", "config"]:
    #
    #                                 # recognize key to give a file import as value
    #                                 print("Give a file.yaml as value")
    #                                 continue
    #                             """ end division """
    #                         except Exception as e:
    #                             print("[ CRAWL_DIVISION ]", str(e))
    #
    #                     elif v == "":
    #                         self.sprint("You didn't give me any Value", mode=self.modus)
    #                     else:
    #                         # call for complete help overview
    #                         # wrong arguments as input ...:...
    #                         crawl_usage()
    #                     break
    #
    #                 elif i in crawler_help:
    #                     # crawl help
    #                     crawl_usage()
    #                     break
    #                 elif i in crawler_commands:
    #                     self.sprint("i also need a value. E.g: {}:{{ value }}".format(i), mode=self.modus)
    #                     break
    #                 else:
    #                     self.sprint("None recognized command", mode=self.modus)
    #
    #         else:
    #
    #             # No valid input by user
    #             self.sprint("None Input from user", mode=self.modus)
    #
    #     except Exception as e:
    #         print("[ {}_EXCEPTION ]".format(self.__class__.__name__), str(e))
    #



class Arachnida(TargetFunctions, CrawlerFunctions, Nimbus, Sprint):
    """
    Arachnida Mother Crawler Object as Abstract as Possible
    @design-pattern:
    @inherritence:
    @methods: [ ]
    @gets-orders:
    """
    # __target_history_in_crawl_mode

    def __init__(self, url=None, ip=None):
        """[ CRAWLER ] Just Crawling Around"""
        import argparse
        super(Arachnida, self).__init__()
        Nimbus.__init__(self)

        self.name = "Crawler Object"
        self.modus = "[ CRAWLER|MODE ]"
        self.colors = {"back": Back.RED, "fore": Fore.GREEN}

        self.session_id = id(self)
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "
        self.session_crawl = True

        self.queue = self._queue_crawler

        from Core.banners import Banners
        Banners.arachnida()

        self.sprint("ACTIVATED", mode=self.modus)

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework {}".format(self.modus), description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
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

    def q(self):
        """[ QUEUE ] The Queue Object size/print/remove/clear/?"""

        try:
            command = self.command.split()[1]
            self.sprint("Printing the Queue Object for: {}".format(self.__class__.__name__), mode=self.modus)

            if command == "size":
                self.sprint(self.queue.qsize(), mode=self.modus)
            elif command == "print":
                self.sprint(self.queue.queue)
            elif command == "remove":
                val = self.command.split()[2]
                self.queue.queue.remove(val)
                self.sprint("Item has been removed from the Queue: {}".format(val))
            elif command == "clear":
                self.queue.queue.clear()
                self.sprint("Queue is emptied")
            elif command == "?":
                self.sprint("[!] The Queue is {}empty".format("" if self.queue.empty() else "NOT"))
                self.sprint("[!] The Size of the Queue is currently: {}".format(self.queue.qsize()))
                self.sprint("[!] The Unfninished tasks: {}".format(self.queue.unfinished_tasks))
            else:
                self.sprint("Unknown Queue Command. Try 'q size/print/remove/clear/?'", mode=self.modus)
        except IndexError as e:
            self.sprint("[ {} ] {}".format(self.__class__.__name__, str(e)), mode=self.modus)
        return

    def leave(self):
        """[ LEAVE ] Mode Gently """
        self.session_crawl = False
        return self

    def list(self):
        """[ LIST_FIND ] List targets in Crawler|Mode and use"""
        import re
        from veryprettytable import VeryPrettyTable

        table = VeryPrettyTable(["crawled", "id", "name", "ip", "url", "notes"])
        table.align = "l"
        table.padding_width = 2

        # pre-defined key_commands
        key_command = ["save", "crawl", "queue"]

        # get the complete command minus the command itself
        print(self.command.split())

        # check is something is filled
        if len(self.command.split()[1:]) >= 1:

            # there are arguments given
            # check how many arguments ar given
            print(len(self.command.split()[1:]))

            # loop over the arguments
            for i in self.command.split()[1:]:

                ''' *** START: key commands *** '''
                # check if argument is a key_command argument
                if i in key_command:

                    # argument [ i ] is a key_command
                    print("This is a Key Command: {}".format(i))

                    if i == "save":
                        """ Save to my _saved_list """
                        print("Save this to the Target-List")

                    elif i == "discover":
                        """ Send to Spider to .discover() """
                        print("Trying to Discover if there is a known CMS or Framework installed")

                    elif i == "crawl":
                        """ Send to Spider to .crawl() """
                        print("Directly send to the crawler")

                        # check in which index number the given command i is indexed
                        num = self.command.split()[1:].index(i)
                        # print index number as integer in array of command .split()
                        print(num)

                        # pop the command out of the array, So there will only be a string IF given key:value is 1 argument
                        doc = self.command.split().pop(num)

                        # get Key and Value of the String
                        k, v = doc.split(":")[0], doc.split(":", 1)[1]

                        # cursor to get the url value fore the given filter
                        urls = db.find({"target_{}".format(k):v})

                        # loop over the given documents to get the url value of each document
                        for url in urls:

                            # firstly print the gotten url
                            print(" [!] Found URL and Queue: {}".format(url["target_url"]))

                            # send directly to the crawler to crawl the URL
                            # self.crawl(url=url["target_url"])
                            self._queue_crawler.queue.append(url["target_url"])

                            print(" ... ... appended URL to the Queue")

                    elif i == "queue":
                        """ Update Tasksand update _queue_crawler"""
                        print("Put into the Queue to process when possible")
                        # check in which index number the given command i is indexed
                        num = self.command.split()[1:].index(i)
                        # print index number as integer in array of command .split()
                        print(num)

                        # pop the command out of the array, So there will only be a string IF given key:value is 1 argument
                        doc = self.command.split().pop(num)

                        # get Key and Value of the String
                        k, v = doc.split(":")[0], doc.split(":", 1)[1]

                        # cursor to get the url value fore the given filter
                        urls = db.find({"target_{}".format(k):v})

                        # loop over the given documents to get the url value of each document
                        for url in urls:

                            # firstly print the gotten url
                            print(" [!] Found URL and Queue: {}".format(url["target_url"]))

                            # send directly to the crawler to crawl the URL
                            # self.crawl(url=url["target_url"])
                            self._queue_crawler.queue.append(url["target_url"])

                            print(" ... ... appended URL to the Queue")

                    continue

                # else
                # check if argument is a Key:Value
                elif re.search(":", i):

                    # argument is a Key:Value
                    print(i)

                    # create a Key and Value of the given argument
                    k, v = i.split(":")[0], i.split(":", 1)[1]

                    print(" Printing the Key: {}".format(k))
                    print(" Printing the Value: {}".format(v))

                    found = db.find({"target_{}".format(k):v})

                    for i in found:
                        table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"], i["target_note"]])
                    print("\n{}\n".format(table))
                    continue

                print("Unknown command")

        else:
            # there are None arguments given
            self.sprint("No arguments are given!", mode=self.modus)


    # def crawl(self):
    #     """[ START ] crawling the pinned Target! 'crawl help' for more info"""
    #
    #     import re
    #
    #     # crawl [commands]:[value]
    #     crawler_help = ["help", "?", "-h", "--help"]
    #     crawler_commands = ["url", "name", "id", "ip", "pinned", "file", "config"]
    #
    #     try:
    #         # check of er iets is ingevuld
    #         if len(self.command.split()[1:]) >= 1:
    #
    #             # er is iets gevuld
    #             # is het een commando zonder value of een Key:Value
    #             for i in self.command.split()[1:]:
    #
    #                 # check if command has arguments crawl key but no :Value
    #                 if re.search(":", i):
    #
    #                     # split every argument in Key and Value
    #                     k, v = i.split(":", 1)[0], i.split(":", 1)[1]
    #
    #                     # check if key is in commands
    #                     if k in crawler_commands and v != "":
    #                         print("The command is {}".format(k))
    #                         print("The value what was given is: {}".format(v))
    #
    #                         try:
    #                             """ Start devision """
    #                             # if key is url
    #                             if k == "url":
    #
    #                                 # check in database if url is known
    #                                 found = db.find({"target_{}".format(k):v})
    #
    #                                 # print length of found
    #                                 print(found.count())
    #
    #                                 if found.count() == 0:
    #                                     self.sprint("[!] This URL is not found in the database", mode=self.modus)
    #                                     add_url = input("[?] Do you want to add this URL to the database? Y/n ").lower()
    #
    #                                     while True:
    #                                         if add_url == "Y".lower() or add_url == "Yes".lower():
    #                                             self.sprint("Create a new Target Model Object and pus it into the Database")
    #                                             from Modules.Target.models import AddTarget
    #                                             target = AddTarget(url=v)
    #                                             db.insert_one(target.__dict__)
    #                                             break
    #                                         elif add_url == "n".lower() or add_url == "no".lower():
    #                                             self.sprint("No? Then we will proceed without the Database ;)", mode=self.modus)
    #                                             break
    #                                         else:
    #                                             print("Try again!")
    #                                             continue
    #
    #
    #
    #                                     """ Hier gebleven """
    #
    #                                 elif found.count() == 1:
    #
    #                                     # just found 1 target record
    #                                     # therefor we can proceed with this target
    #                                     print("found just 1 record")
    #                                     print("return a table with this records")
    #                                     print("is this correct? shall we proceed? Y/n ")
    #                                     break
    #                                 else:
    #                                     # found multiple records
    #                                     # loop over the found records
    #                                     for url in found:
    #                                         print(url)
    #
    #                                 continue
    #
    #                             elif k in ["name", "id", "pinned", "ip"]:
    #
    #                                 # check in database if target is known
    #
    #                                     # if yes, check for target_url to crawl
    #                                     # if no
    #                                         # print Err. No such target_{{ key }}
    #                                         # do you want to save this target and append more info?
    #                                 continue
    #                             elif k in ["file", "config"]:
    #
    #                                 # recognize key to give a file import as value
    #                                 print("Give a file.yaml as value")
    #                                 continue
    #                             """ end division """
    #                         except Exception as e:
    #                             print("[ CRAWL_DIVISION ]", str(e))
    #
    #                     elif v == "":
    #                         self.sprint("You didn't give me any Value", mode=self.modus)
    #                     else:
    #                         # call for complete help overview
    #                         # wrong arguments as input ...:...
    #                         crawl_usage()
    #                     break
    #
    #                 elif i in crawler_help:
    #                     # crawl help
    #                     crawl_usage()
    #                     break
    #                 elif i in crawler_commands:
    #                     self.sprint("i also need a value. E.g: {}:{{ value }}".format(i), mode=self.modus)
    #                     break
    #                 else:
    #                     self.sprint("None recognized command", mode=self.modus)
    #
    #         else:
    #
    #             # No valid input by user
    #             self.sprint("None Input from user", mode=self.modus)
    #
    #     except Exception as e:
    #         print("[ {}_EXCEPTION ]".format(self.__class__.__name__), str(e))
    #
    # def target(self):
    #     """[ TARGETS ] To define the targets, search here"""
    #     from veryprettytable import VeryPrettyTable
    #     import re
    #     """
    #         target list
    #         target shell
    #         target crawled
    #     """
    #     # get command target
    #
    #         # key commands
    #             # shell; go to Target() --shell
    #             # crawled, done
    #
    #         # global list, to hold all last searched targets _id
    #         # by key:value
    #
    #     # pre-defined tables with headers IF we find any data
    #     # table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
    #     table = VeryPrettyTable()
    #     table.align = "l"
    #     table.padding_width = 2
    #
    #     try:
    #
    #         key_commands = ["list", "shell", "done", "current", "q"]
    #
    #         if len(self.command.split()[1:]) >= 1:
    #
    #             # there is input given by user
    #             # check if arguments are key:value or key_command
    #
    #             # first print length of arguments
    #             print(len(self.command.split()[1:]))
    #
    #             # loop over arguments that is given
    #             for i in self.command.split()[1:]:
    #
    #                 # check if it is a key:value argument
    #                 if re.search(":", i):
    #
    #                     # then print out the key and value
    #                     k, v = i.split(":", 1)[0], i.split(":", 1)[1]
    #
    #                     if v != "":
    #
    #                         # check in database for search query
    #                         found = db.find({"target_{}".format(k):v})
    #
    #                         # if you found something in database return it
    #                         if found.count() != 0:
    #
    #                             # is you found records, create the table for cli
    #                             table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
    #
    #                             # and then; loop over the records
    #                             # loop over the foundings
    #                             for i in found:
    #                                 print(i)
    #                                 table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])
    #
    #                             # print the table
    #                             print("\n{}\n".format(table))
    #
    #                         # if count is 0
    #                         else:
    #                             self.sprint("Nothin found in the database what matched your search-query")
    #                     else:
    #                         self.sprint("No input for value found. E.g. url:http://www.example.com")
    #
    #                 # else if no : in argument, maybe its a key_command
    #                 elif i in key_commands:
    #
    #                     # print out the key_command to do something with it later
    #                     # print("It is a Key Command")
    #                     # print(i)
    #
    #                     #             key_commands = ["list", "shell", "done", "current", "q"]
    #
    #                     if i == "done":
    #                         doc = {"crawler": {"crawled":"done"}}
    #                         continue
    #                     elif i == "q":
    #                         doc = {"crawler": {"crawled":"q"}}
    #                         continue
    #                     elif i == "current":
    #                         doc = {"crawler": {"crawled":"crawling"}}
    #                         continue
    #                     elif i == "shell":
    #                         print("Go to Target Shell Mode")
    #                     elif i == "list":
    #                         print("Target List")
    #
    #                     # retrieve from database
    #                     found = db.find(doc)
    #
    #                     # First check if any records are found by counting
    #                     if i.count() == 0:
    #                         print("Nothing in Store. Double-Check everything")
    #                     else:
    #
    #                         # loop over the foundings
    #                         for i in found:
    #                             print(i)
    #
    #                     break
    #
    #                 # if no Key:Value or Key_command input then what?
    #                 else:
    #                     self.sprint("Wrong Key:Value argument or Command. Try to use 'target help' for more info")
    #
    #         else:
    #
    #             # there is no argumnet input given
    #             self.sprint("None comment given", mode=self.modus)
    #
    #     except Exception as e:
    #         print(str(e))
    #
    # def config(self):
    #     """[ config ] Crawler plugins on/off or true/false"""
    #
    #     """
    #         config list
    #         config name:on name:off name:true name:false
    #         config save
    #     """
    #     pass
    #
    # def set(self):
    #     pass
    #
    #     # set target:ip:234234
    #     # set target:name:hubbabubba
    #     # set target:url:http:///www.example.com
    #     # targets["targets].find_one({"url": "http://www.example.com"})
    #
    #     # targets["targets].update({"pinned": "true"}, {$set: {"pinned": "false"}})
    #     # targets["targets].update({"url": "http://www.example.com"}, {$set: {"pinned": "true"}})
    #
    # # def pinned(self):
    # #     """[ PINNED ] Return the Pinned target to be exploited"""
    # #     print(self.session_target)



# if __name__ == '__main__':
#     t = Target(ip="149.210.192.240")
#     print(t)
#
#     t.name = "QI.NL"
#     t.url = "http://www.----.nl"
#     # t.ip = "149.210.192.240"
#
#     print(t)
#     print(t.id)
#
