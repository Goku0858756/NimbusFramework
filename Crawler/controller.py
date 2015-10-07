__author__ = 'N05F3R4TU'
import requests
# from bs4 import BeautifulSoup
import argparse, sys

def usage():
    """
    Print Usage for Arachnida
    :return:
    """
    print('\033c')
    print('''

    Arachnida <command> [<args>]

    ## The most commonly used commands are:

    command         Description
    =======================================
    crawl            Lets crawl a site *_*

    ''')

def usage_crawler():
    """
    Print Usage for Arachnida
    :return:
    """
    print('\033c')
    print('''

    crawl <option> [<args>]

    ## The most commonly used commands are:

    command         Description
    =======================================
    url            Give me a URL !!

    ''')

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
            usage=usage())
        self.parser.add_argument('module', help='Give me a module to use ;)')

        self.args = self.parser.parse_args(sys.argv[1:2])
        if not hasattr(self, self.args.module):
            print('\033c')
            print('Unrecognized module')
            self.parser.print_help()
            exit(1)

        getattr(self, self.args.module)()

    def crawl(self):
        """
        Crawl Method
        :return:
        """
        print('\033c')
        parser = argparse.ArgumentParser(prog="", usage=usage_crawler(), description="", epilog=None, add_help=True, argument_default=None)
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
    # Temporary
    __set_all_href = {}

    def __init__(self, *args):
        self.__dict__ = self.__shared_infromation
        args = args[0]

        self.name = ''
        self.session = requests.Session()
        self.user_agent = self.user_agent()

        self.pid = ''
        self.state = ''
        self.depth = 0
        self.base = True
        self.url = self.session.get(url=args.url)

        self.encode = self.encoding()
        self.redirect = self.is_redirect()
        self.status = self.status_code()
        self.cookie = self.cookies()
        self.header = self.headers()

    def __str__(self):
        return str(self.__shared_infromation)

    def update(self, **kwargs):
        self.__shared_infromation.update(kwargs)

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

    def url_check(self, url):
        from urllib.parse import urlparse

        parsed_url = urlparse(url=url)
        if parsed_url.netloc == '' or parsed_url.netloc != self.__set_base_url['netloc']:
            print('[ NO NETLOC    ]', parsed_url.netloc)
        else:
            print('[ MATCH NETLOC ]', parsed_url.netloc)
        if parsed_url.scheme == '' or parsed_url.scheme != self.__set_base_url['scheme']:
            print('[ NO SCHEME    ] ', parsed_url.scheme)
        else:
            print('[ MATCH SCHEME ]', parsed_url.scheme)
        if parsed_url.path != '':
            print('[ PATH ]', parsed_url.path)
        print(self.__set_base_url['scheme'])
        print(self.__set_base_url['netloc'])

    def url_validate(self):
        from urllib.parse import urlparse

        split = urlparse(url=self.url.url, allow_fragments=False)
        if self.base != False:
            self.__set_base_url.update(scheme=split.scheme, netloc=split.netloc, path=split.path, query=split.query, fragment=split.fragment)
            self.base = False
        self.__set_all_href.update(scheme=split.scheme, netloc=split.netloc, path=split.path, query=split.query, fragment=split.fragment)

    def encoding(self):
        self.update(encoding=self.url.encoding)

    def is_redirect(self):
        self.update(is_redirect=self.url.is_redirect)

    def status_code(self):
        self.update(status_code=self.url.status_code)

    def cookies(self):
        self.update(cookies=self.url.cookies)

    def headers(self):
        self.update(headers=self.url.headers)

    def write_to_json(self):
        # TODO: Get BaseUrl Name
        # TODO: Create File with BaseUrl Name
        # TODO: Create Index in JSON with Crawl Header Information
        # TODO: Create Base Object and structure
        pass

    def write_to_xml(self):
        pass

if __name__ == '__main__':
    obj = Arachnida()
