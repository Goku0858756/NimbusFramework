__author__ = 'N05F3R4TU'
import argparse
import sys
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
        parser.add_argument("-B", dest="base_dom", action="store_true", default=False,
                            help="[ TRUE/FALSE ] Base domain only")

        args = parser.parse_args(sys.argv[2:])
        print(parser)
        print(args)
        print('Running a crawler, url=%s' % args.url)

        crawler = Crawler(args)




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
    _set_all_href_dict = {}

    _set_all_href   = []
    _set_url_intern = []
    _set_url_href   = []

    queue = Queue()

    def __init__(self, *args):
        import requests
        self.__dict__ = self.__shared_infromation
        self.args = args[0]

        self.name = ''
        self.session = requests.Session()
        self.useragent = self.user_agent()

        self.pid = ''
        self.state = ''
        self.depth = 0
        self.base = True
        self.base_dom = self.args.base_dom
        self.url = self.session.get(url=self.args.url)
        self.url_validate()

        self.encode = self.encoding()
        self.redirect = self.is_redirect()
        self.status = self.status_code()
        self.cookie = self.cookies()
        self.header = self.headers()

        if self.url:
            self.run(url=self.url)

    def __str__(self):
        return str(self.__shared_infromation)

    def __del__(self):
        print(self.__class__.__name__, "Destructed")

    def update(self, **kwargs):
        self.__shared_infromation.update(kwargs)

    def run(self, url=None):
        from bs4 import BeautifulSoup

        if url != None:
            for self._set_all_href in set([href.get('href') for href in BeautifulSoup(url.text).find_all('a')]):
                self.queue.queue.append(self.url_check(self._set_all_href))
<<<<<<< HEAD

            print(len(self._set_all_href))
            print(self._set_all_href)
            print("Calling for Baby Spider")
            sleep(3)
=======
>>>>>>> e9686bf4c09b9550791c44d10f2412e99d97067d
            spiderling = Spiderling()
        else:
            assert "[ ASSERTION ERROR ] URL is None"
        return

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
        Check IF given URL is a (( HTTP )) or (( FTP )) or (( MAILTO ))
        Check IF given URL is a http or https
        """
        from urllib.parse import urlparse
        import re
        parsed_url = urlparse(url=url)
<<<<<<< HEAD

        # Internal Link
        if not parsed_url.netloc and not parsed_url.scheme and parsed_url.path:
            return str(
                "{}://{}{}".format(self.__set_base_url['scheme'], self.__set_base_url['netloc'], parsed_url.path))
        else:
            assert "[ ASSERTION ERROR #1 ]", parsed_url

        # External Link
        if parsed_url.netloc and parsed_url.netloc != self.__set_base_url['netloc']:
            if re.match('//', url):
                return '{}:{}'.format(self.__set_base_url['scheme'], url)
            else:
                assert "[ ASSERTION ERROR #2 ]", parsed_url
            return url
        else:
            assert "[ ASSERTION ERROR #3 ]", parsed_url

        # Full Link is Correct
        return url

    def url_validate(self):
        from urllib.parse import urlparse

        split = urlparse(url=self.url.url, allow_fragments=True)
=======

        # Internal Link
        if not parsed_url.netloc and not parsed_url.scheme and parsed_url.path:
            return "{}://{}{}".format(self.__set_base_url['scheme'], self.__set_base_url['netloc'], parsed_url.path)

        # External Link
        if parsed_url.netloc and parsed_url.netloc != self.__set_base_url['netloc']:
            if re.match('//', url):
                return '{}:{}'.format(self.__set_base_url['scheme'], url)
            return url

    def url_validate(self):
        from urllib.parse import urlparse
        split = urlparse(url=self.url.url, allow_fragments=False)
>>>>>>> e9686bf4c09b9550791c44d10f2412e99d97067d
        if self.base != False:
            self.__set_base_url.update(scheme=split.scheme, netloc=split.netloc, path=split.path, query=split.query, fragment=split.fragment)
            self.base = False
        self._set_all_href_dict.update(scheme=split.scheme, netloc=split.netloc, path=split.path, query=split.query, fragment=split.fragment)

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
    Een Lijst met welke Links al bezocht zijn
        Als nieuwe link niet in Lijst staat Voeg toe in Queue
    """
    def __init__(self):

        if self.queue.empty() != True:
            self.crawl()

    def crawl(self):
        from bs4 import BeautifulSoup
        import requests

        try:

            for link in set([href.get('href') for href in
                             BeautifulSoup(requests.get(url=self.queue.get(block=True)).text).find_all('a')]):
                # print(self.url_check(url=link))
                # print(link)

<<<<<<< HEAD
                if self.url_check(url=link) not in self._set_all_href:
                    self._set_all_href.append(self.url_check(url=link))
                    self.queue.queue.append(self.url_check(url=link))

        except Exception as e:
            print("[ EXCEPTION ERROR IN SPIDERLING ]", str(e))

        finally:
            print("[ QUEUE ]:", self.queue.qsize())
            print("[ ARRAY ]:", len(self._set_all_href))
=======
        for link in set([href.get('href') for href in BeautifulSoup(requests.get(self.queue.get(block=True)).text).find_all('a')]):
            print(link)

            if link not in self._set_all_href:
                self._set_all_href.append(link) and self.queue.put(link)
>>>>>>> e9686bf4c09b9550791c44d10f2412e99d97067d

        # Recursion
        if self.queue.empty() == False:
            self.crawl()
        else:
            print("[ EMPTY ] Queue is Empty", self.queue.qsize())



if __name__ == '__main__':
    obj = Arachnida()