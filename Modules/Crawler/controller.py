#!/usr/bin/env python
from colorama import Fore, Back, Style, init
from pymongo import MongoClient
from Modules.Target.controller import TargetFunctions
from nimbus import Nimbus
from sprint import Sprint

from Modules.Crawler.functions import CrawlerFunctions

mongo = MongoClient('localhost', port=27017, connect=True)
db = mongo["targets"]["targets"]

__author__ = 'N05F3R4TU'

init(autoreset=True)


def crawl_usage():
    import subprocess, os

    # subprocess.call("./crawl_usage.sh", shell=True)
    full_path = os.path.dirname(os.path.realpath(__file__))
    os.system("cat {}/{}".format(full_path, "crawl_usage.sh"))



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

        # pre-defined find filter with key and values
        find_filter = {}

        # get the complete command minus the command itself
        # print(self.command.split())

        # check is something is filled
        if len(self.command.split()[1:]) >= 1:

            # there are arguments given
            # check how many arguments ar given
            # print(len(self.command.split()[1:]))

            # loop over the arguments
            for i in self.command.split()[1:]:

                ''' *** START: key commands *** '''
                # check if argument is a key_command argument
                if i in key_command:

                    # argument [ i ] is a key_command
                    # print("This is a Key Command: {}".format(i))

                    if i == "save":
                        """ Save to my _saved_list """
                        print("Save this to the Target-List")
                        print("[ Not Working Yet ]")

                    elif i == "discover":
                        """ Send to Spider to .discover() """
                        print("Trying to Discover if there is a known CMS or Framework installed")

                    elif i == "crawl":
                        """ Send to Spider to .crawl() """
                        self.sprint(" [!] Sending Spiders to the Target", mode=self.modus)

                        # check in which index number the given command i is indexed
                        num = self.command.split()[1:].index(i)
                        # print index number as integer in array of command .split()
                        # print(num)

                        # pop the command out of the array, So there will only be a string IF given key:value is 1 argument
                        doc = self.command.split().pop(num)

                        # get Key and Value of the String
                        k, v = doc.split(":")[0], doc.split(":", 1)[1]

                        # cursor to get the url value fore the given filter
                        urls = db.find({"target_{}".format(k):v})

                        # loop over the given documents to get the url value of each document
                        for url in urls:

                            # firstly print the gotten url
                            self.sprint(" [!] Found URL and Queue: {}".format(url["target_url"]), mode=self.modus)

                            # send directly to the crawler to crawl the URL
                            self._queue_crawler.queue.append(url["target_url"])
                            self.sprint(" [!] ... appended URL to the Queue", mode=self.modus)
                            self.sprint(" [!] ... Send to Spiders")

                            # start the crawl with the spiders
                            self.crawl()

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
                    # print(i)

                    # create a Key and Value of the given argument
                    k, v = i.split(":")[0], i.split(":", 1)[1]

                    # print(" Printing the Key: {}".format(k))
                    # print(" Printing the Value: {}".format(v))

                    found = db.find({"target_{}".format(k):v})

                    for i in found:
                        table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"], i["target_note"]])

                    print("\n{}\n".format(table))
                    continue

                print("Unknown command")

        else:
            # there are None arguments given
            self.sprint("No arguments are given!", mode=self.modus)

            try:
                self.sprint("\r\n")
                docs = db.find()

                for target in docs:
                    table.add_row([target["target_pinned"], target["_id"], target["target_name"], target["target_ip"], target["target_url"], target["target_note"]])
            except Exception as e:
                print(str(e))


            print("\n{}\n".format(table))