__author__ = 'N05F3R4TU'
from sprint import Sprint

class SQLIController(Sprint):
    """
    Nimbus SQL Injection Controller Object
    """
    def __init__(self, *args):
        import os
        super().__init__()
        self.id = id(self)
        self.name = "Nimbus SQL Injection Controller Object"
        self.args = args[0]

        self.full_path = os.path.dirname(os.path.realpath(__file__))
        self.file = "server.sh"

        # TEMP: Print Complete Dict
        self.sprint(self.args)

        if self.args["target"] != None:
            self.sprint(self.args["target"])
        else:
            self.sprint("######### SQLI || ERROR")

        self.sprint("Object ID: %s is Created" % self.id)

    def __del__(self):
        self.sprint("Object ID: %s is Destroyed, Object-Name is: %s" % (self.id, self.__class__.__name__))
        return self

    def target(self):
        """
        Example: python sqlmap.py -u [<TARGET>]
        :return:
        """
        pass

    def dork(self):
        """
        Example: Use Google-Dorks
        :return:
        """
        pass

    def smoke_test(self):
        """
        Do a Smoke-Test first with these Parameters
        :return:
        """
        pass

    def thread_level(self, level=1):
        """
        How many Threads to use. Standard 1 Thread
        :return: thread level 1-5
        """
        if level > 5:
            """Max thread level is 5"""
            threads = 5
        elif level <= 0:
            threads = 1
        else:
            threads = level
        return threads

    def tamper(self):
        """
        Example: sqlmap -u 'http://www.site.com:80/search.cmd?form_state=1’ --level=5 --risk=3 -p 'item1' --tamper=apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,bluecoat,chardoubleencode,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,randomcomments,securesphere,space2comment,space2dash,space2hash,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
        Tamper with the following given Tamper-Scripts
        :return:
        """
        tamper_dict = {
            "general": ["apostrophemask", "apostrophenullencode", "base64encode", "between", "chardoubleencode", "charencode", "charunicodeencode", "equaltolike", "greatest", "ifnull2ifisnull", "multiplespaces", "nonrecursivereplacement", "percentage", "randomcase", "securesphere", "space2comment", "space2plus", "space2randomblank", "unionalltounion", "unmagicquotes"],
            "MSSQL": ["between", "charencode", "charunicodeencode", "equaltolike", "greatest", "multiplespaces", "nonrecursivereplacement", "percentage", "randomcase", "securesphere", "sp_password", "space2comment", "space2dash", "space2mssqlblank", "space2mysqldash", "space2plus","space2randomblank", "unionalltounion", "unmagicquotes"],
            "MySQL": ["between", "bluecoat", "charencode", "charunicodeencode", "concat2concatws", "equaltolike", "greatest", "halfversionedmorekeywords", "ifnull2ifisnull", "modsecurityversioned", "modsecurityzeroversioned", "multiplespaces", "nonrecursivereplacement", "percentage", "randomcase", "securesphere", "space2comment", "space2hash", "space2morehash", "space2mysqldash", "space2plus", "space2randomblank", "unionalltounion", "unmagicquotes", "versionedkeywords", "versionedmorekeywords", "xforwardedfor"]
        }
        return tamper_dict

    def risk_level(self):
        """
        Risk Level of being detected. Standard risk level is 1
        :return:
        """
        pass

    def optimization(self):
        """
        Turn on all optimization switches
        :return: -o
        """
        return "-o"

    def timeouts(self, seconds="30"):
        """
        Timeouts to act like a human
        :return: seconds to wait is standard 30 seconds
        """
        return "--timeout= {}".format(seconds)

    def proxy(self):
        """
        Use a given proxy
        :return:
        """
        pass

    def user_agent(self):
        """
        User Agents randomize
        :return:
        """
        pass

    def tor(self):
        """
        Use TOR to anonymize, Use SOCKS5 with PySocks and Selenium
        :return:
        """
        pass

    def mobile(self, mob=False):
        """
        Imitate smartphone through HTTP
        :return:
        """
        if mob != False:
            return "--mobile"
        return mob

    def output(self, ext="csv"):
        """
        Output File standard as .csv
        :param ext: csv, sql, html
        :return: --dump-format
        """
        return "--dump-format=%s" % ext

    def output_dir(self, dir):
        """
        Output directory to Dump to
        :return: --output-dir
        """
        return "--output-dir={}".format(dir)

    def save(self):
        """
        Save Config to a Config file
        :return:
        """
        return "--save"

    def batch(self):
        """
        Never Ask for input
        :return: True/False
        """
        return "--batch"

    def forms(self):
        """
        Parse and Test forms on target URL
        :return: True/False
        """
        return "--forms"

    def waf(self):
        """
        Check for WAF and Intrusion Prevention Systems
        :return:
        """
        return "--check-waf"

    def wizard(self):
        """
        Wizard Interface Mode
        :return: --wizard
        """
        return "--wizard"