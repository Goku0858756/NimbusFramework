__author__ = 'N05F3R4TU'
import requests
from bs4 import BeautifulSoup
import argparse, os, sys


class Arachnida(object):
    """
    Controller Object
    """

    def __init__(self):
        """
        Controller Constructor
        :return:
        """
        self.parser = argparse.ArgumentParser(
            prog="Controller Object",
            description='You can use this Controller to select Modules',
            usage="USAGE TEXT")
        self.parser.add_argument('module', help='Give me a module to use ;)')

        self.args = self.parser.parse_args(sys.argv[1:2])
        if not hasattr(self, self.args.module):
            os.system("clear")
            print('Unrecognized module')
            self.parser.print_help()
            exit(1)

        getattr(self, self.args.module)()

    def crawl(self):
        """
        Crawl Method
        :return:
        """
        os.system('clear')
        parser = argparse.ArgumentParser(prog="", usage="Usage Text", description="", epilog=None, add_help=True, argument_default=None)
        parser.add_argument("url")
        parser.add_argument("-d", "--depth", dest="depth")
        parser.add_argument("-i", "--in", dest="input", help="Give the spider input data")
        parser.add_argument("-o", "--out", dest="output", help="To send the output to a file")
        parser.add_argument("--db", dest="db", help="Send Log to Database when finished")
        parser.add_argument("-b", dest="base", help="Base domain only")

        args = parser.parse_args(sys.argv[2:])
        print('Running a crawler, url=%s' % args.url)

        crawler = Crawler(args)
        crawler.run()


class Crawler(object):

    __shared_infromation = {}
    __set_base_url = {}
    __set_intern_href = []
    __set_extern_href = []

    def __init__(self, *args):
        args = args[0]

        self.name = ''
        self.session = requests.Session()
        self.user_agent = self.user_agent()
        self.pid = ''
        self.state = ''
        self.depth = 0
        self.url = args.url

    def run(self):
        print(self.url)

    def user_agent(self):
        import random
        """
        User-Agents Function. Call this to get a Random User-Agent
        :return: a dictionary:
        Example: {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}
        For more User-Agent Strings: http://www.useragentstring.com/pages/useragentstring.php
        """
        agents = ['Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36']
        return {'User-Agent': random.choice(agents)}

    def url_validate(self):
        pass


if __name__ == '__main__':
    obj = Arachnida()