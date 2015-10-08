__author__ = 'N05F3R4TU'
import requests
# from bs4 import BeautifulSoup
import argparse, sys
from time import sleep

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


# TODO: This Object Must be a Core Controller Object
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




# TODO: The Crawler Object Must be a Abstract-Interface which Can be Implemented and Used by <script>-plugins
class Crawler(object):
    from queue import Queue
    """
    This Crawler Object:
     - GETs a Job/Task to crawl a url + [options] + [<args>]
     - The run() Function Must be Called to start the Sub-Crawler (spiderlings)
    This Crawler Object HAS a ((SHARED_QUEUE)) and the ((SHARED_SETS)) for the urls [ All, Internal, External ]
     - The Spiderling Object(s) Will Crawl the Website/Url in Depth and Append/Report to the Master-Crawler-Object
    """

    __shared_infromation = {}
    __set_base_url = {}

    __set_all_href   = {}
    __set_url_intern = []
    __set_url_href   = []

    queue = Queue()

    def __init__(self, *args):
        self.__dict__ = self.__shared_infromation
        self.args = args[0]

        self.name = ''
        self.session = requests.Session()
        self.useragent = self.user_agent()

        self.pid = ''
        self.state = ''
        self.depth = 0
        self.base = True
        self.url = self.session.get(url=self.args.url)
        self.url_validate()

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
        from bs4 import BeautifulSoup
        """
        Start Crawling Process
        :return:
        """

        # TODO: Set session_id, session_name

        for url in set([href.get('href') for href in BeautifulSoup(self.url.text).find_all('a')]):
            self.queue.queue.append(url)

        # TODO: Create a Function With States [ base_url || url_validate || queue_urls || birth_spiderling ]

        print("Creating a Spiderling")
        sleep(3)

        spiderling = Spiderling(self.args)

    def user_agent(self):
        # TODO: THIS WILL BECOME A SEPERATE PLUGIN
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
        """
        Check Every given URL for the following:
            Check IF given URL is a Internal-Link or External
            Check IF given URL is a (( XPath )) or (( Relative Path )) or (( Full Path ))
            Check IF given URL is a (( HTTP )) or (( FTP )) or (( MAILTO ))
            Check IF given URL is a http or https

                Check given *args for settings
                    IF correct Divide URLs by Passing URL to (( self.url_validate() )) function
        :param url:
        :return:
        """
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
        """
        Validate and SPLIT the given URL [ INPUT FROM COMMAND-LINE ]
        """
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


class Spiderling(Crawler):
    """
    This Child of Crawler called Spiderling Will POP
    an HREF from the Mother-Crawler-Object and will gather all HREFs from the given URL
     - Will Filter URLs by Internal_url && External_url with the Methods, which are Passed by
       the Mother-Object [ inherritence ]

     - The URLs will be stored into a Set() in the Mother-Crawler-Object

    """

    def __init__(self, *args):
        Crawler.__init__(self)
        self.__dict__ = Crawler.__dict__

        self.user_agent = "Fun"
        print(self.queue.queue)

        # self.pop_url = self.queue.queue.pop()
        #
        # print("POP ::::", self.pop_url)
        # sleep(3)
        #
        # self.url_check(url=self.pop_url)




if __name__ == '__main__':
    obj = Arachnida()


"""
crawl basis pagina [ doe alles in een Set() ]
    Plaats van een Set() naar de Queue()
        Maak een Spiderling session aan, POP van de Queue(), MAAR ook APPEND naar een Lijst met de AL Gecrawlde URLs

        Als de NEW URL niet in de (((AL_CRAWLED_LIST)) zit, voeg toe aan de moeder_Set()

            Wanneer Queue None is ::

                Zet Set() over naar Queue() en Repeat
"""