#!/usr/bin/env python
from colorama import Fore, Back, Style, init
from nimbus import Nimbus
from sprint import Sprint
import argparse
from time import sleep
from veryprettytable import VeryPrettyTable
from pymongo import MongoClient


mongo = MongoClient("localhost", port=27017, connect=True)
db = mongo["targets"]["targets"]
archive = mongo["targets"]["archive"]

__author__ = 'N05F3R4TU'
__version__ = "2.1"
__license__ = "Nimbus Corp"

init(autoreset=True)



class TargetFunctions:

    def __init__(self):
        super(TargetFunctions, self).__init__()
        self.name = "Target Functions object"

    def remove(self):
        """[ REM ] Remove from Hitlist"""
        import re

        # pre-defined tables with headers IF we find any data
        table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
        table.align = "l"
        table.padding_width = 2

        # remember all objects by _id
        object_id = []

        # pre-defined find filter
        # this is meant to find the requested records easier from the database
        rem_filter = {}

        # get command and check if there are multiple arguments minus self.command[0]
        if self.command.split()[1:]:

            # loop over the arguments and check if there is a Key:Value
            for a in self.command.split()[1:]:

                print(a)
                print("-"*50)

                # check k:v
                if re.search(":", a):

                    k, v = a.split(":")[0], a.split(":", 1)[1]
                    print(k)
                    print(v)
                    print("-"*50)

                    # update the filter dictionary
                    rem_filter.update({"target_{}".format(k):v})

            # get the Findings from the Database
            findings = db.find(rem_filter)

            print(findings)
            print("-"*50)

            # loop over every document you have found and display it in a Table on CLI
            for i in findings:

                print(i)

                # append the object_id array by _id as key
                object_id.append(i["_id"])

                # add every document as row to the table
                table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])

            # print the table
            print("\n{}\n".format(table))

            # loop for acknowledge
            while True:

                # ask if these documents are to be removed ?
                acknowledge = input("Are these document(s) the ones you want to remove ?: Y/n ").lower()

                if acknowledge == "y".lower() or acknowledge == "yes".lower():

                    # if yes loop over the array with all object _id(s)
                    for v in object_id:

                        doc = db.find_one({"_id":v})
                        archive.insert_one(doc)
                        db.remove(doc)

                    print("all done")
                    break
                elif acknowledge == "n".lower() or acknowledge == "no".lower():
                    print("Shheeeuuuhh")
                    break
                else:
                    print("Try again!")
                    continue
        else:
            self.sprint("You forgot to add options", mode=self.modus)


    def edit(self):
        """[ EDIT ] Edit my a Target"""

        """ Psuedo Code

            Check If Something is filled
            edit .... ?
                check if there is a something filled
                edit ip:123.123.321.22 ... ?
                    |_ IF yes get Records for PART1
                    |_ IF no return Err Message

                check if is > sign
                edit ip:123.123.321.22 > ...?
                    |_ IF yes AND no PART2 Err Message: You didnt give me anything to update it with;
                    |_ IF yes ... break it into PART1 (filter) and PART2 (update// $set)


        # TARGET --shell

            edit    [ ...:... ...:... ] > [ ...:... ]
            remove  [ ...:... ]
                        |- return record(s)
                            |_ Are you sure?
            add     ip:... name:... url:...
            find    [ ...:... ...:... ]

        # ADD

            vpn     [ ..:.. ]
            server  [ ..:.. ]
            user    [ ..:.. ]

        # OPTIONS

            modules             <- return a list of available modules
            modules:crawler     <- return a list of available options crawler module
            modules:crawler xpath:True base_only:True tag_forms:True

            plugin
            user
            proxy
            vpn
            target
            template


        ## CliDl

            command     category:type:name:additional limit filter filter -f function_name()
        """
        import re

        # pre-defined tables with headers IF we find any data
        table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
        table.align = "l"
        table.padding_width = 2

        # pre-defined object variable to connect the gotten record and update it by _id
        # there can be multiple _id(s) to be updated so therefore it will be a array
        object_id = []

        if self.command.split()[1:]:
            # there is more then index[0]
            # check if there is a > $gt

            # if self.command.find(">"):
            if re.search(">", self.command):

                # there is a $gt sign and can be split up
                splitted = self.command.split(">", 1)

                # splitted PART1 contains the original command
                # so only split and get the given filters
                # Also how many filters are given ?
                part1 = splitted[0].split()

                # print how many filters are given MINUS the original command ?
                # print(len(part1[1:]))

                # print everything after the original command
                # print(part1[1:])

                # create a dictionary to fill with the complete query
                filter_part1 = {}

                # Loop over the filters if there are more the 1
                if len(part1[1:]) >= 1:

                    # loop over every filter
                    for f in part1[1:]:

                        # get the key, value for each filter
                        k, v = f.split(":")[0], f.split(":", 1)[1]

                        # and update the dictionary to get the records IF exists
                        # WATCH the target_{} string
                        filter_part1.update({"target_{}".format(k):v})

                # save foundings into records variable
                records = db.find(filter_part1)

                # loop over findings
                for i in records:

                    # update the object_id array
                    # which holds the given objects to be updated
                    object_id.append(i["_id"])

                    # and display the finding into the pre-defined tables
                    table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])

                # print the table for the user
                # print("\n{}\n".format(table))

                # print the given object id(s)
                # print(object_id)

                # we got the first part and record(s)
                # now for the second part to update the requested record(s)
                part2 = splitted[1].split()

                # print the length of how many field we have to update
                # print(len(part2))

                # create a dictionary to fill with the complete update_query
                filter_part2 = {}

                # check if length update arguments are more then 1
                if len(part2) >= 1:

                    # for every field update get key, value
                    for f in part2:

                        # get the key, value for each filter
                        k, v = f.split(":")[0], f.split(":", 1)[1]

                        # and update the dictionary to get the records IF exists
                        # WATCH the target_{} string
                        filter_part2.update({"target_{}".format(k):v})

                    # get the objects to be updated by object_id array
                    # get the fields from part2 which have to be updated
                    # do a findAndUpdate of the documents with $set
                    # do not update full documents, just update fields or add non-existing fields to the document

                    # update the records in the database as Many documents
                    db.update_many(filter_part1, {"$set": filter_part2})

            else:

                if re.search(":", self.command[1:]):

                    # get records for PART1 but there is no PART2!
                    print("getting records from database")

                    # pre-defined find filter for part1 without part2
                    # this is meant to find the requested records easier then directly updating the database
                    find_filter = {}

                    # get all filters minus indexx[0] the command
                    find = self.command.split()[1:]

                    # print the length of the filters
                    print(len(find))

                    # do a loop to get a complete key, value query to send to the database
                    for f in find:

                        # for each loop get the k, v and update it to the dictionary
                        k, v = f.split(":")[0], f.split(":", 1)[1]

                        # update the dictionary
                        find_filter.update({"target_{}".format(k):v})

                    # get records from the database
                    findings = db.find(find_filter)

                    # loop over the records to create a table at cli
                    for i in findings:

                        # and display the finding into the pre-defined tables
                        table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])

                    # print the table for the user
                    print("\n{}\n".format(table))
                else:
                    print("Your arguments to filter from the database are not correct. I need a Key:Value")

        else:
            self.sprint("You forgot to add options", mode=self.modus)


    def list(self):
        """[ LIST ] Me My Targets (last 20)? """

        table = VeryPrettyTable(["pinned", "id", "name", "ip", "url", "notes"])
        table.align = "l"
        table.padding_width = 2

        try:
            self.sprint("\r\n")
            db = mongo["targets"]["targets"].find()

            for target in db:
                table.add_row([target["target_pinned"], target["_id"], target["target_name"], target["target_ip"], target["target_url"], target["target_note"]])
        except Exception as e:
            print(str(e))
        finally:
            db.close()

        print("\n{}\n".format(table))

    # def list(self):
    #     """[ FIND ] Me the Target I want"""
    #     import re
    #     from veryprettytable import VeryPrettyTable
    #
    #     table = VeryPrettyTable(["pinned", "id", "name", "ip", "url", "notes"])
    #     table.align = "l"
    #     table.padding_width = 2
    #
    #     # pre-defined key_commands
    #     key_command = ["pin", "remove", "save"]
    #     # save; for later
    #     # remove; move to archive in db
    #     # pin; target set to pin in document; this is the target we gonna use
    #
    #     # get the complete command minus the command itself
    #     # print(self.command.split())
    #
    #     # if command_array is 1 or more arguments
    #     if len(self.command.split()[1:]) >= 1:
    #
    #         # if argument have :  then; db_filter
    #         # if argument is key_command  then; take right action
    #         # if nothing found;     then; give error message back
    #         # if argument is unknown    then; return error message
    #
    #
    #     # User input in NOT 1 or more
    #     else:
    #
    #         """ None user input"""
    #         self.sprint("None User Input given", mode=self.modus)



    def active(self):
        """[ ACTIVE ] The poor Bastards, They will never see me coming"""
        self.sprint("Victim which are being attacked")

    def add(self):
        """[ ADD ] New Victim to attack"""
        import yaml

        self.function_name = "add"
        session_target_add = True

        parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Their surrender is inevitable", add_help=True)

        while session_target_add:
            try:
                if not self.command.split()[1:]:
                    self.sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
                    break
                elif self.command.split()[1:]:
                    parser.add_argument("-n", dest="name", action="store", default=None, help="Add target into system by Name")
                    parser.add_argument("-c", dest="contract", action="store", default=None, help="Add target by contract")
                    parser.add_argument("-i", dest="ip", action="store", default=None, help="Add target by IP")
                    parser.add_argument("-u", dest="url", action="store", default=None, help="Add target by URL. E.g: http://www.victim.com")
                    # parser.add_argument("-t", dest="template", action="store_true", default=False, help="Add target by complete Template")
                    parser.add_argument("-t", dest="file", type=argparse.FileType(mode="r"))

                    args = parser.parse_args(self.command.split()[1:])

                    """ here we import the method and call the object with our args """
                    from Modules.Target.models import AddTarget
                    # instantiate target model object
                    target = AddTarget()

                    # if the option from file is True then read from it at first
                    if args.file:

                        # check if file is a yaml file
                        print("Yaml File is given")
                        sleep(2)

                        # if it is a yaml file then; read it
                        with args.file as f:
                            x = yaml.load(f)

                            # check if target name
                            if x["name"]:

                                # check if there are given multiple names
                                if len(x["name"]) > 1:

                                    # print Err. Customer can only have one name per record (it can have multiple IPs and URLs)
                                    print("Please change the Customer File. A Customer can only have one name to be reffered to")
                                else:
                                    # add name to the customer model object
                                    target.target_name = x["name"][0]
                            else:
                                print("None Name given")

                            # check if ip is given
                            if x["ip"]:

                                # check if given multiple ip's
                                if len(x["ip"]) > 1:
                                    # save ip as array
                                    target.target_ip = x["ip"]
                                else:
                                    # save just 1 ip to the target.template
                                    target.target_ip = x['ip'][0]
                            else:
                                print("None IP given")

                            # check if url is given
                            if x["url"]:

                                # check if given multiple url's
                                if len(x["url"]) > 1:
                                    # save url as array
                                    target.target_url = x["url"]
                                else:
                                    # save just 1 url to the target.template
                                    target.target_url = x['url'][0]
                            else:
                                print("None Url given")

                            # check if dns is given
                            if x["dns"]:

                                # check if given multiple dns's
                                if len(x["dns"]) > 1:
                                    # save dns as array
                                    target.target_dns = x["dns"]
                                else:
                                    # save just 1 dns to the target.template
                                    target.target_dns = x['dns'][0]
                            else:
                                print("I am missing dns(s) for the target")

                            if x["id"]:
                                if len(x["id"]) != 1:
                                    print("Error. I can handle only one ID per Target")
                                else:
                                    target.target_contract = x["id"]

                        # print __str__ target model object to see if it is alright
                        # print(target.__dict__)

                    else:
                        print(args)
                        if args.name != None:
                            target.target_name = args.name
                        if args.contract != None:
                            target.target_contract = args.contract
                        if args.ip != None:
                            target.target_ip = args.ip
                        if args.url != None:
                            target.target_url = args.url

                    while True:
                        pin = input("Do you want to use this target now?: Y/n ").lower()

                        if pin == "y".lower() or pin == "yes".lower():
                            target.target_pinned = True
                            db.find_one_and_update({"target_pinned":True}, {"$set": {"target_pinned": False}}, multi=True, safe=True)
                            db.insert_one(vars(target))
                            print("[!] Target Pinned")
                            break
                        elif pin == "n".lower() or pin == "no".lower():
                            db.insert_one(vars(target))
                            print("No? Maybe Later ;)")
                            break
                        else:
                            print("Try again!")
                            continue

            except Exception as e:
                self.sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
            finally:
                break



class TargetShell(TargetFunctions, Nimbus, Sprint):
    """
        Target Shell Objectq
    """

    def __init__(self):
        """
        Target Shell Object
        :return:
        """
        super(TargetShell, self).__init__()
        self.name = "Target Shell Object"
        self.modus = "[ TARGET|MODE ]"
        self.colors = {"back":Back.BLUE, "fore":Fore.YELLOW}

        self.session_id = id(self)
        self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "
        self.session_target = True

        self.queue = self._queue_target

        self.sprint("{} Activated".format(self.name), mode=self.modus)

        self.parser = argparse.ArgumentParser(prog="Nimbus Framework {}".format(self.modus), description="The search has already been started !", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
        self.parser.add_argument('command', help="Use command to begin")

        while self.session_target:
            self.command = input(self.session_name)
            if not self.command:
                self.sprint("No Command Given", mode=self.modus)
                continue
            else:
                import re

                if re.match("-", self.command.split()[0]):
                    self.sprint("Wrong! Dont use OPTIONS but choose a COMMAND")
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

                            self.sprint("Unrecognized command")
                            self.sprint("try again pall")
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
            if attr not in ["usage", "__init__", "__del__", "__str__", "save_state", "methods", "sprint"]:
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
                self.sprint("[!] The Queue is {} empty".format("" if self.queue.empty() else "NOT"))
                self.sprint("[!] The Size of the Queue is currently: {}".format(self.queue.qsize()))
                self.sprint("[!] The Unfninished tasks: {}".format(self.queue.unfinished_tasks))
            else:
                self.sprint("Unknown Queue Command. Try 'q size/print/remove/clear/?'", mode=self.modus)
        except IndexError as e:
            self.sprint("[ {} ] {}".format(self.__class__.__name__, str(e)), mode=self.modus)
        return

    def leave(self):
        """[ LEAVE ] This mode Gently"""
        self.session_target = False


# class Target(Nimbus, Sprint):
#
#     def __init__(self):
#         """[ TARGET ] Looking for VICTIMS"""
#         import argparse
#         super()
#         Sprint.modus = "[ TARGET|MODE ]"
#         self.name = "Target Shell Object"
#         self.modus = "[ TARGET|MODE ]"
#         self.colors = {"back":Back.BLUE, "fore":Fore.YELLOW}
#         self.session_name = "nimbus " + self.colors['back'] + self.colors['fore'] + "{}".format(self.modus) + Style.RESET_ALL + " \> "
#
#         self.session_id = id(self)
#         self.session = True
#
#         self.sprint("ACTIVATED")
#
#         self.parser = argparse.ArgumentParser(prog="Nimbus Framework [CRAWLER|MODE ]", description="Need it any description?", argument_default=None, epilog="Nimbus // Rain with Rage, Exploit with Love")
#         self.parser.add_argument('command', help="Use command to begin")
#
#         while self.session:
#             self.command = input(self.session_name)
#             if not self.command:
#                 self.sprint("No Command Given", mode=self.modus)
#                 continue
#             else:
#                 import re
#
#                 if re.match("-", self.command.split()[0]):
#                     self.sprint("Wrong! Dont use OPTIONS but choose a COMMAND")
#                     print(self.usage())
#                     continue
#                 elif self.command.split()[0] == "?":
#                     print(self.usage())
#                 else:
#                     self.args = self.parser.parse_args(self.command.split()[0:1])
#
#                     try:
#                         if hasattr(self, self.args.command):
#                             """ Maybe the Most Important Code of the Whole Framework """
#                             getattr(self, self.args.command)()
#
#                         elif not hasattr(self, self.args.command):
#
#                             self.sprint("Unrecognized command")
#                             self.sprint("try again pall")
#                             self.sprint("*" * 40 + "\n")
#                             print(self.usage(), "\n")
#                             self.sprint("*" * 40 + "\n")
#                             continue
#                         else:
#                             print("%s\n%s\n%s" % ("*"*40, "* If you see this message, something went HORRIBLY wrong! Call for help!", "*"*40))
#                     except Exception as e:
#                         print(str("[ {}_EXCEPTION ]".format(self.__class__.__name__)).upper(), str(e))
#
#     def __str__(self):
#         self.sprint(self.__dict__)
#
#     def __del__(self):
#         self.sprint(self.__class__.__name__, "Destroyed")
#         return self
#
#     def usage(self):
#         """Usage Coomment String"""
#         import inspect
#         from Core.banners import Banners
#         from veryprettytable import VeryPrettyTable
#         banner = Banners()
#
#         commands = VeryPrettyTable(["Command", "Description"])
#         commands.align = "l"
#         commands.padding_width = 2
#
#         banner.randomize()
#         for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
#             if attr not in ["usage", "__init__", "__del__", "__str__", "save_state", "methods", "sprint"]:
#                 commands.add_row([attr, getattr(self, attr).__doc__])
#         return commands
#
#     def remove(self):
#         """[ REM ] Remove from Hitlist"""
#         import re
#
#         # pre-defined tables with headers IF we find any data
#         table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
#         table.align = "l"
#         table.padding_width = 2
#
#         # remember all objects by _id
#         object_id = []
#
#         # pre-defined find filter
#         # this is meant to find the requested records easier from the database
#         rem_filter = {}
#
#         # get command and check if there are multiple arguments minus self.command[0]
#         if self.command.split()[1:]:
#
#             # loop over the arguments and check if there is a Key:Value
#             for a in self.command.split()[1:]:
#
#                 print(a)
#                 print("-"*50)
#
#                 # check k:v
#                 if re.search(":", a):
#
#                     k, v = a.split(":")[0], a.split(":", 1)[1]
#                     print(k)
#                     print(v)
#                     print("-"*50)
#
#                     # update the filter dictionary
#                     rem_filter.update({"target_{}".format(k):v})
#
#             # get the Findings from the Database
#             findings = db.find(rem_filter)
#
#             print(findings)
#             print("-"*50)
#
#             # loop over every document you have found and display it in a Table on CLI
#             for i in findings:
#
#                 print(i)
#
#                 # append the object_id array by _id as key
#                 object_id.append(i["_id"])
#
#                 # add every document as row to the table
#                 table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])
#
#             # print the table
#             print("\n{}\n".format(table))
#
#             # loop for acknowledge
#             while True:
#
#                 # ask if these documents are to be removed ?
#                 acknowledge = input("Are these document(s) the ones you want to remove ?: Y/n ").lower()
#
#                 if acknowledge == "y".lower() or acknowledge == "yes".lower():
#
#                     # if yes loop over the array with all object _id(s)
#                     for v in object_id:
#
#                         doc = db.find_one({"_id":v})
#                         archive.insert_one(doc)
#                         db.remove(doc)
#
#
#                     print("all done")
#                     break
#                 elif acknowledge == "n".lower() or acknowledge == "no".lower():
#                     print("Shheeeuuuhh")
#                     break
#                 else:
#                     print("Try again!")
#                     continue
#         else:
#             self.sprint("You forgot to add options", mode=self.modus)
#
#
#     def edit(self):
#         """[ EDIT ] Edit my a Target"""
#
#         """ Psuedo Code
#
#             Check If Something is filled
#             edit .... ?
#                 check if there is a something filled
#                 edit ip:123.123.321.22 ... ?
#                     |_ IF yes get Records for PART1
#                     |_ IF no return Err Message
#
#                 check if is > sign
#                 edit ip:123.123.321.22 > ...?
#                     |_ IF yes AND no PART2 Err Message: You didnt give me anything to update it with;
#                     |_ IF yes ... break it into PART1 (filter) and PART2 (update// $set)
#
#
#         # TARGET --shell
#
#             edit    [ ...:... ...:... ] > [ ...:... ]
#             remove  [ ...:... ]
#                         |- return record(s)
#                             |_ Are you sure?
#             add     ip:... name:... url:...
#             find    [ ...:... ...:... ]
#
#         # ADD
#
#             vpn     [ ..:.. ]
#             server  [ ..:.. ]
#             user    [ ..:.. ]
#
#         # OPTIONS
#
#             modules             <- return a list of available modules
#             modules:crawler     <- return a list of available options crawler module
#             modules:crawler xpath:True base_only:True tag_forms:True
#
#             plugin
#             user
#             proxy
#             vpn
#             target
#             template
#
#
#         ## CliDl
#
#             command     category:type:name:additional limit filter filter -f function_name()
#         """
#         import re
#
#         # pre-defined tables with headers IF we find any data
#         table = VeryPrettyTable(["pinned", "id", "name", "ip", "url"])
#         table.align = "l"
#         table.padding_width = 2
#
#         # pre-defined object variable to connect the gotten record and update it by _id
#         # there can be multiple _id(s) to be updated so therefore it will be a array
#         object_id = []
#
#         if self.command.split()[1:]:
#             # there is more then index[0]
#             # check if there is a > $gt
#
#             # if self.command.find(">"):
#             if re.search(">", self.command):
#
#                 # there is a $gt sign and can be split up
#                 splitted = self.command.split(">", 1)
#
#                 # splitted PART1 contains the original command
#                 # so only split and get the given filters
#                 # Also how many filters are given ?
#                 part1 = splitted[0].split()
#
#                 # print how many filters are given MINUS the original command ?
#                 # print(len(part1[1:]))
#
#                 # print everything after the original command
#                 # print(part1[1:])
#
#                 # create a dictionary to fill with the complete query
#                 filter_part1 = {}
#
#                 # Loop over the filters if there are more the 1
#                 if len(part1[1:]) >= 1:
#
#                     # loop over every filter
#                     for f in part1[1:]:
#
#                         # get the key, value for each filter
#                         k, v = f.split(":")[0], f.split(":", 1)[1]
#
#                         # and update the dictionary to get the records IF exists
#                         # WATCH the target_{} string
#                         filter_part1.update({"target_{}".format(k):v})
#
#                 # save foundings into records variable
#                 records = db.find(filter_part1)
#
#                 # loop over findings
#                 for i in records:
#
#                     # update the object_id array
#                     # which holds the given objects to be updated
#                     object_id.append(i["_id"])
#
#                     # and display the finding into the pre-defined tables
#                     table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])
#
#                 # print the table for the user
#                 # print("\n{}\n".format(table))
#
#                 # print the given object id(s)
#                 # print(object_id)
#
#                 # we got the first part and record(s)
#                 # now for the second part to update the requested record(s)
#                 part2 = splitted[1].split()
#
#                 # print the length of how many field we have to update
#                 # print(len(part2))
#
#                 # create a dictionary to fill with the complete update_query
#                 filter_part2 = {}
#
#                 # check if length update arguments are more then 1
#                 if len(part2) >= 1:
#
#                     # for every field update get key, value
#                     for f in part2:
#
#                         # get the key, value for each filter
#                         k, v = f.split(":")[0], f.split(":", 1)[1]
#
#                         # and update the dictionary to get the records IF exists
#                         # WATCH the target_{} string
#                         filter_part2.update({"target_{}".format(k):v})
#
#                     # get the objects to be updated by object_id array
#                     # get the fields from part2 which have to be updated
#                     # do a findAndUpdate of the documents with $set
#                     # do not update full documents, just update fields or add non-existing fields to the document
#
#                     # update the records in the database as Many documents
#                     db.update_many(filter_part1, {"$set": filter_part2})
#
#             else:
#
#                 if re.search(":", self.command[1:]):
#
#                     # get records for PART1 but there is no PART2!
#                     print("getting records from database")
#
#                     # pre-defined find filter for part1 without part2
#                     # this is meant to find the requested records easier then directly updating the database
#                     find_filter = {}
#
#                     # get all filters minus indexx[0] the command
#                     find = self.command.split()[1:]
#
#                     # print the length of the filters
#                     print(len(find))
#
#                     # do a loop to get a complete key, value query to send to the database
#                     for f in find:
#
#                         # for each loop get the k, v and update it to the dictionary
#                         k, v = f.split(":")[0], f.split(":", 1)[1]
#
#                         # update the dictionary
#                         find_filter.update({"target_{}".format(k):v})
#
#                     # get records from the database
#                     findings = db.find(find_filter)
#
#                     # loop over the records to create a table at cli
#                     for i in findings:
#
#                         # and display the finding into the pre-defined tables
#                         table.add_row([i["target_pinned"], i["_id"], i["target_name"], i["target_ip"], i["target_url"]])
#
#                     # print the table for the user
#                     print("\n{}\n".format(table))
#                 else:
#                     print("Your arguments to filter from the database are not correct. I need a Key:Value")
#
#         else:
#             self.sprint("You forgot to add options", mode=self.modus)
#
#
#     def list(self):
#         """[ LIST ] My My Targets"""
#
#         table = VeryPrettyTable(["pinned", "id", "name", "ip", "url", "notes"])
#         table.align = "l"
#         table.padding_width = 2
#
#         try:
#             self.sprint("\r\n")
#             db = mongo["targets"]["targets"].find()
#
#             for target in db:
#                 table.add_row([target["target_pinned"], target["_id"], target["target_name"], target["target_ip"], target["target_url"], target["target_note"]])
#         except Exception as e:
#             print(str(e))
#         finally:
#             db.close()
#
#         print("\n{}\n".format(table))
#
#     def active(self):
#         """[ ACTIVE ] The poor Bastards, They will never see me coming"""
#         self.sprint("Victim which are being attacked")
#
#     def leave(self):
#         """[ LEAVE ] Mode Gently"""
#         self.session = False
#
#     def add(self):
#         """[ ADD ] New Victim to attack"""
#         import argparse
#         import yaml
#
#         self.function_name = "add"
#         session_target_add = True
#
#         parser = argparse.ArgumentParser(prog="{} function".format(self.function_name.upper()), description="Their surrender is inevitable", add_help=True)
#
#         while session_target_add:
#             try:
#                 if not self.command.split()[1:]:
#                     self.sprint("Try to use `{} -h` for more option".format(self.function_name.lower()))
#                     break
#                 elif self.command.split()[1:]:
#                     parser.add_argument("-n", dest="name", action="store", default=None, help="Add target into system by Name")
#                     parser.add_argument("-c", dest="contract", action="store", default=None, help="Add target by contract")
#                     parser.add_argument("-i", dest="ip", action="store", default=None, help="Add target by IP")
#                     parser.add_argument("-u", dest="url", action="store", default=None, help="Add target by URL. E.g: http://www.victim.com")
#                     # parser.add_argument("-t", dest="template", action="store_true", default=False, help="Add target by complete Template")
#                     parser.add_argument("-t", dest="file", type=argparse.FileType(mode="r"))
#
#                     args = parser.parse_args(self.command.split()[1:])
#
#                     """ here we import the method and call the object with our args """
#                     from Modules.Target.models import AddTarget
#                     # instantiate target model object
#                     target = AddTarget()
#
#                     # if the option from file is True then read from it at first
#                     if args.file:
#
#                         # check if file is a yaml file
#                         print("Yaml File is given")
#                         sleep(2)
#
#                         # if it is a yaml file then; read it
#                         with args.file as f:
#                             x = yaml.load(f)
#
#                             # check if target name
#                             if x["name"]:
#
#                                 # check if there are given multiple names
#                                 if len(x["name"]) > 1:
#
#                                     # print Err. Customer can only have one name per record (it can have multiple IPs and URLs)
#                                     print("Please change the Customer File. A Customer can only have one name to be reffered to")
#                                 else:
#                                     # add name to the customer model object
#                                     target.target_name = x["name"][0]
#                             else:
#                                 print("None Name given")
#
#                             # check if ip is given
#                             if x["ip"]:
#
#                                 # check if given multiple ip's
#                                 if len(x["ip"]) > 1:
#                                     # save ip as array
#                                     target.target_ip = x["ip"]
#                                 else:
#                                     # save just 1 ip to the target.template
#                                     target.target_ip = x['ip'][0]
#                             else:
#                                 print("None IP given")
#
#                             # check if url is given
#                             if x["url"]:
#
#                                 # check if given multiple url's
#                                 if len(x["url"]) > 1:
#                                     # save url as array
#                                     target.target_url = x["url"]
#                                 else:
#                                     # save just 1 url to the target.template
#                                     target.target_url = x['url'][0]
#                             else:
#                                 print("None Url given")
#
#                             # check if dns is given
#                             if x["dns"]:
#
#                                 # check if given multiple dns's
#                                 if len(x["dns"]) > 1:
#                                     # save dns as array
#                                     target.target_dns = x["dns"]
#                                 else:
#                                     # save just 1 dns to the target.template
#                                     target.target_dns = x['dns'][0]
#                             else:
#                                 print("I am missing dns(s) for the target")
#
#                             if x["id"]:
#                                 if len(x["id"]) != 1:
#                                     print("Error. I can handle only one ID per Target")
#                                 else:
#                                     target.target_contract = x["id"]
#
#                         # print __str__ target model object to see if it is alright
#                         # print(target.__dict__)
#
#                     else:
#                         print(args)
#                         if args.name != None:
#                             target.target_name = args.name
#                         if args.contract != None:
#                             target.target_contract = args.contract
#                         if args.ip != None:
#                             target.target_ip = args.ip
#                         if args.url != None:
#                             target.target_url = args.url
#
#                     while True:
#                         pin = input("Do you want to use this target now?: Y/n ").lower()
#
#                         if pin == "y".lower() or pin == "yes".lower():
#                             target.target_pinned = True
#                             db.find_one_and_update({"target_pinned":True}, {"$set": {"target_pinned": False}}, multi=True, safe=True)
#                             db.insert_one(vars(target))
#                             print("[!] Target Pinned")
#                             break
#                         elif pin == "n".lower() or pin == "no".lower():
#                             db.insert_one(vars(target))
#                             print("No? Maybe Later ;)")
#                             break
#                         else:
#                             print("Try again!")
#                             continue
#
#             except Exception as e:
#                 self.sprint(Exception("[ {} ]".format(self.function_name.upper()), str(e)))
#             finally:
#                 break