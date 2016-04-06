__author__ = 'N05F3R4TU'
from Plugins.NimbusCrawler.spider_setting import SpiderSetting
# from Plugins.NimbusCrawler.spider_functions import SpiderFunction
# from Plugins.NimbusCrawler.spider_enum import SpiderEnum
from Plugins.NimbusCrawler.spider_data import SpiderData

# from spider_setting import SpiderSetting
# from spider_data import SpiderData

import requests
from bs4 import BeautifulSoup
from datetime import datetime

from multiprocessing import Process

import os
from time import sleep

class Spider(SpiderSetting, SpiderData):

    def __init__(self, url):
        self.object_id = id(self)
        self.name = "My Little Ichy Spider"
        self.this_path = os.path.dirname(os.path.realpath(__file__))

        # inherit Settings
        self.settings = SpiderSetting()
        self.data = SpiderData()

        # Create as Session for the base URL
        self.session = requests.Session()

        # Verbose output
        self.verbose = self.settings.verbose

        # Get URL
        self.url = url

        # origin URL
        self.origin = {"scheme": '', "netloc": '', "path": '', "params": '', "query": '', "fragment": ''}

        # Save the URLs
        # self.hrefs_intern = [self.url]  # first url in list
        self.hrefs_all    = []

        # queue object to iterate later for vulnerabilities
        from queue import Queue
        self.queue_to_audit = Queue()

        # put the base url into the Queue to start
        self.queue_to_audit.put(self.url)

        # update all methods
        self.iter_funcs = []
        self.functions()
        self.validate_url_orgin()

    def __enter__(self):
        print("Entered The Spider Caves")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(len(self.hrefs_all))

    def __str__(self):
        print(self.__dict__)

    # def __del__(self):
    #     print(self.__class__.__name__, "Destroyed")
    #     return self

    def check_for_old_session(self):

        print("Checking for Older Spider Sessions")
        sleep(3)

        import socket
        ip = socket.gethostbyname(self.origin["netloc"])
        print("[ IP ]:  {}".format(ip))

        # save IP of this URL to Data Object
        self.data.target_ip = ip

        sleep(3)

        from Plugins.IPConversion.controller import ip_to_int
        as_int = ip_to_int(socket.gethostbyname(self.origin["netloc"]))
        print(as_int)

        sleep(3)

        sess_path = "Sessions/Crawler/"

        # Is there a archived session of this IP?
        archive_file = os.path.isfile("{}{}.txt".format(sess_path, str(as_int)))
        # print(archive_file)
        sleep(3)

        if archive_file:
            with open("{}{}.txt".format(sess_path, str(as_int)), mode="r") as archive:
                for e, link in enumerate(archive.readlines()):
                    # print(str("[ {}   ] - {}".format(e, link)).strip())
                    self.hrefs_all.append(link)

            print(len(self.hrefs_all))
            sleep(3)

        else:
            print("None Archive Session Found")

    def crawl(self):
        """This function is the start function to Spider URLs Threaded"""

        self.check_for_old_session()

        try:

            if self.queue_to_audit.qsize() > 0:

                # for e, t in enumerate(range(0, int(self.settings.threads))):
                # for t in range(0, 1):
                for t in range(0, int(self.settings.threads)):

                    print(t)

                    t = Process(target=self.spider, args=(5,))
                    # t1.name = "ProcessThread-{}".format(e)
                    t.daemon = False
                    t.start()
                    t.join()

                    print("*"*50)
                    print("PID: {}".format(t.pid))
                    print("ALIVE: {}".format(t.is_alive()))

            else:
                print("There is nothing in the Queue")
        except Exception as e:
            print(self.__class__.__name__.__getattribute__(self))
            print(e)



    def spider(self, delay):
        """This function will be the Thread itself"""
        """ Worker """

        print("started a new Thread to Crawl @ {}".format(datetime.now()))
        print("Delay is : {} seconds".format(delay))
        sleep(delay)

        try:

            while bool(self.queue_to_audit.qsize() > 0):

                # get a url from queue, outside the try catch block for scope
                url_from_queue = self.queue_to_audit.get(block=True)

                req_url = self.session.get(url=url_from_queue)

                # if status_code is 200; then crawl
                hrefs = [link.get("href") for link in BeautifulSoup(req_url.text, "html.parser").find_all("a")]

                checked = list(map(
                    self.url_check,
                    hrefs
                ))

                for href in checked:
                    self.save_links(url=href)

                print("*"*50)
                print("QUEUE: {}".format(self.queue_to_audit.qsize()))
                print("ARRAY: {}".format(len(self.hrefs_all)))

        # Exception if User kills the process
        except KeyboardInterrupt:
            print("\t\t\t [ SPIDER INTERRUPTED BY USER ]\n\n")
        except Exception as e:
            print("[ SPIDER EXCEPTION ]", str(e))
        finally:
            self.data.dump_to_file(self.hrefs_all)





        #
        # while True:
        #     # prepared url variable
        #     url_from_queue = ""
        #
        #     try:
        #
        #         while self.queue_to_audit.qsize() > 0:
        #
        #             # get a url from queue, outside the try catch block for scope
        #             url_from_queue = self.queue_to_audit.get(block=True)
        #             # print("[ FROM QUEUE ]", str(url_from_queue))
        #
        #             # TODO: Pre check Request to URL
        #             # @pre-request-check based on url.base
        #             # every request outside the base_url is not allowed
        #
        #             try:
        #                 print("[ QUEUE  ]:", str(self.queue_to_audit.qsize())) if self.verbose else ""
        #                 print("[ LINKS  ]:", str(len(self.hrefs_all))) if self.verbose else ""
        #                 print("*"*60) if self.verbose else ""
        #
        #                 req_url = self.session.get(url=url_from_queue)
        #
        #                 # if site is not there and give error other then 200 skip the next part
        #                 if req_url.status_code != 200:
        #                     # print(req_url.status_code)
        #                     continue
        #
        #                 # if status_code is 200; then crawl
        #                 hrefs = [link.get("href") for link in BeautifulSoup(req_url.text, "html.parser").find_all("a")]
        #                 # print(self.session.headers)
        #
        #                 checked = list(map(
        #                     self.url_check,
        #                     hrefs
        #                 ))
        #
        #                 for i in checked:
        #                     if i:
        #                         self.save_links(url=i)
        #
        #             except ConnectionAbortedError as e:
        #                 print("[ EXCEPTION ] Connection Aborted Err", str(e))
        #                 continue
        #             except TimeoutError as e:
        #                 print("[ Err. TimeOut ]", str(e))
        #                 continue
        #             except KeyboardInterrupt:
        #                 # if keyboard interruption is detected, first save the data
        #                 self.dump_to_file()
        #                 break
        #
        #     except Exception as e:
        #         # print("[ Mother Of All Exceptions ]", str(e))
        #         # print(url_from_queue)
        #         # NimbusDebug.save_log("{} {}".format(self.__class__.__name__, str(e)))
        #         # sleep(5)
        #         # continue
        #         print("Exception hero")
        #         raise Exception(e)
        #     finally:
        #         print("Dumping file in Finnaly")
        #         self.dump_to_file()

    def url_check(self, url):
        """
        Check IF given URL is a (( HTTP )) or (( FTP )) or (( MAILTO ))
        Check IF given URL is a http or https
        """
        from urllib.parse import urlparse, urljoin
        import re

        parsed_base = urlparse(url=self.url, allow_fragments=False)
        parsed_url  = urlparse(url=url, allow_fragments=False)

        wrong_paths = ["#", None]
        social_media = ["youtube.com", "www.youtube.com", "facebook.com", "www.facebook.com", "twitter.com", "www.twitter.com", "pinterest.com", "www.pinterest.com", "plus.google.com", "instagram.com", "www.instagram.com"]

        try:
            # TODO: not accepted
            if url in wrong_paths:
                print("[ FOUT     ]:    ", str(url)) if self.verbose else ""
                return False

            # TODO: internal:   /dir/dir/   or /dir/dir/file.html
            # elif not parsed_url.scheme and not parsed_url.netloc and parsed_url.path:
            elif not parsed_url.scheme and not parsed_url.netloc:

                # TODO: root
                if parsed_url.path == "/":
                    print("[ ROOT     ]:    ", str(url)) if self.verbose else ""
                    return True

                # print("[ INTERNAL ]:    ", str(url))
                print("[ INTERNAL ]:    ", str(urljoin(base=parsed_base.geturl(), url=url))) if self.verbose else ""
                # print(url)

                return str(urljoin(base=parsed_base.geturl(), url=url))

            # TODO: full url: http://www.domain.com
            elif re.match(pattern=self.url, string=url) or re.match("https://{}".format(parsed_base.netloc), string=url):
                print("[ FULL URL ]:    ", str(url)) if self.verbose else ""
                return str(url)
                # return str(urljoin(base=parsed_base.geturl(), url=url))
                # print("[ TEST URL ]:    ", str(urljoin(base=parsed_base.geturl(), url=url)))
                # return str(urljoin(base=parsed_base.geturl(), url=url))

            # TODO: sub.domain
            elif parsed_base.scheme and re.search(str(parsed_base.netloc).replace("www.", ""), url) and not re.search("www.", url):
                print("[ SUB.DOM  ]:    ", str(url)) if self.verbose else ""
                # send somewhere else
                return str(url)

            # TODO: xpath
            elif re.match("//", string=str(url)):
                # print("[ XPATH    ]:    ", str(url))
                # check if xpath is base_dom then; True
                # else False
                return str(urljoin(base=parsed_base.geturl(), url=url, allow_fragments=True))
                # return False

            # TODO: javascript
            elif re.match("javascript:", string=url):
                print("[ J.SCRIPT ]:    ", str(url)) if self.verbose else ""
                return False

            # TODO: social media hrefs
            elif parsed_url.netloc in social_media:
                print("[ SOCIAL.M ]:    ", str(url)) if self.verbose else ""
                # if in Settings.Social is True
                # else return False
                # return {"tag":"social", "url": url}
                return False

            else:
                # TODO: everything else
                # print(parsed_url)
                # print("[ EXTERNAL ]:    ", str(url))
                return False

        except Exception as e:
            # print(url)
            # print("[ Err ]", str(e))
            raise Exception(e)

    def save_links(self, url):
        """Check Link if is Intern Href & save to Queue"""
        # import re
        #
        # # if url not in self.hrefs_all:
        # # if re.search("{}".format(str(parsed_base.netloc)), url):
        # if re.search("{}".format(self.origin["netloc"]), url):
        #     if url not in self.hrefs_all:
        #
        #         self.hrefs_all.append(url)
        #         self.queue_to_audit.put(url)
        #
        #         print("[ ADDED           ]    ---     {}".format(url)) if self.verbose else ""
        #         # print("[ ADDED           ]    ---     {}".format(url))
        #     else:
        #         print("[ Err. url found  ]    ---     {}".format(url)) if self.verbose else ""
        #         # print("[ Err. url found  ]    ---     {}".format(url))
        # else:
        #     print("[ Err. Netloc     ]    ---     {}".format(url)) if self.verbose else ""
        #     # print("[ Err. Netloc     ]    ---     {}".format(url))


            # if re.search("{}".format(self.origin["netloc"]), url):
            #     if url not in self.hrefs_all:
            #         self.hrefs_all.append(url)
            #         self.queue_to_audit.put(url)
            #         print("[ ADDED           ]    ---     {}".format(url)) if self.verbose else ""
            #     else:
            #         print("[ Err. url found  ]    ---     {}".format(url)) if self.verbose else ""
            # else:
            #     print("[ Err. Netloc     ]    ---     {}".format(url)) if self.verbose else ""

        if url not in [None, False, True]:
            self.hrefs_all.append(url)
            self.queue_to_audit.put(url)
            print("[ ADDED           ]    ---     {}".format(url)) if self.verbose else ""
        # else:
        #     print(" --- {}".format(url))

    def functions(self):
        """Iterate Through the Spider Methods"""
        import inspect
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["functions", "__init__", "__del__", "__str__", "crawl"]:
                self.iter_funcs.append(attr)

    def validate_url_orgin(self):
        """Parse the original URL as self.origin"""
        from urllib.parse import urlparse

        # for i in ["scheme", "netloc", "path", "params", "query", "fragment"]:
        #     self.origin[i] = vars(urlparse(url=self.url))[i]
        # return self.origin
        g = urlparse(url=self.url)
        self.origin["scheme"] = g.scheme
        self.origin["netloc"] = g.netloc
        self.origin["path"] = g.path
        self.origin["params"] = g.params
        self.origin["query"] = g.query
        self.origin["fragment"] = g.fragment

    # def validate_href_origin(self, anchor):
    #     """Check if the HREF is Internal url or External url"""
    #     from urllib.parse import urlparse
    #     if str(urlparse(url=anchor).netloc).strip() == self.origin["netloc"]:
    #         return True
    #     else:
    #         return False
    #
    # def validate_scheme(self, href):
    #     """Check if URL is HTTPS or HTTP, & fix Broken Scheme"""
    #     from urllib.parse import urlparse, urljoin
    #     s = urlparse(url=href)
    #     try:
    #         # return (str(s.scheme).lower() in self.settings.allow_scheme)
    #         if not s.scheme:
    #             return urljoin("{}://{}".format(self.origin["scheme"], self.origin["netloc"]), href)
    #         else:
    #             return href
    #
    #     except Exception as e:
    #         raise Exception("Scheme not recognised", str(e))
    #
    # def validate_href_type(self):
    #     """Check if HREF is xpath/.../..."""
    #     # map() url over functions to recognize if href is a xpath or something else
    #     pass

    def check_encoding(self):
        """Check encoding/CHARSET is used @ URL"""
        return self.session.get(url=self.url).encoding

    def check_head(self):
        """Check Header of the URL"""
        return self.session.get(url=self.url).headers

    def has_robots(self, url):
        """Check for robots.txt"""
        return requests.get(url="{}/robots.txt".format(url)).ok

    def has_sitemap(self):
        """Check for sitemap.xml"""
        # Check in robots.txt
        # Check as endpoint /sitemap
        # Search for word sitemap on site
        # Search by href sitemap
        # Check for sitemap.xml

    def get_cookies(self):
        """Get Cookies for the URL"""
        pass

    def get_whois(self, *args):
        """Get Whois information"""
        print("WHOISS")
        print(args)

    def get_bannergrab(self):
        """Get banner grabbing information"""
        pass





# # if __name__ == '__main__':
# #     s = Spider(url="http://www.delangejammer.nl")
# #     s.crawl_mode()
# #     # print(s.url_analysis(url="http://www.bol.com"))
# #
# #     """
# #         requests create session
# #         Arachnida gets config file
# #         url_type_recognition
# #         scheme_recognition
# #         url_validation
# #
# #         file create to dump everything
# #         extension_recognition
# #         threading
# #         admin_discover
# #         http_allowed_methods
# #
# #
# #         file_upload [attack]
# #
# #        verdeel beter in grote nodes als modules
# #        verdeel beter naar plugins voor de grote nodes
# #
# #     """

if __name__ == '__main__':
    # s = Spider(url="http://www.wehkamp.nl")
    s = Spider(url="http://www.bol.com")
    # s = Spider(url="https://www.deepcrawl.com") # hmm ?? strange site
    # s = Spider(url="http://www.jimdo.com")
    # s = Spider(url="https://www.jetbrains.com/")
    # s = Spider(url="http://mysmallwebpage.com")   # no www.
    # s = Spider(url="https://jumpcms.wordpress.com")
    # s = Spider(url="http://www.laptopshop.nl/")
    # s = Spider(url="http://www.otto.nl/")
    # s = Spider(url="http://www.klein.nl")

    s.crawl()

    # s = Spider(url="HTTP://www.Python.org/doc/#")

    # s = Spider(url="https://api.github.com/events")

    # s.crawl()
    # s.functions()
    # s.check_encoding()
    # s.check_head()
    # s.get_cookies()

    # print(s.validate_url_orgin())
    # print(s.validate_href_origin())
    # print(s.validate_scheme())
    # print(s.check_robots())

# if __name__ == '__main__':
#     from argparse import ArgumentParser
#
#     parser = ArgumentParser(prog="Nimbus Crawler", add_help=True)
#
#     parser.add_argument("-u", dest="target", action="store", default=None, help="Give a URL as target")
#     parser.add_argument("-t", dest="threads", action="store", type=int, default=3, help="Give me the number of threads to use. max 5 is recommanded")
#     parser.add_argument("-v", dest="verbose", action="store_true", default=False, help="Give al Output in CLI")
#
#     # TODO: Create Groep Output
#     parser.add_argument("-o", dest="output", action="store", default=None, help="Do you want it to dump it to a file")
#
#
#     args = parser.parse_args()
#
#     print(vars(args))
#
