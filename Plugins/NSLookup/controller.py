__author__ = 'N05F3R4TU'
__all__ = ['NSLookup']
import socket


class NSLookup:

    def __init__(self, url=None, ip=None):
        self.id = id(self)
        self.state = None

        if url is not None and ip is None:
            self.by_name(url=url)

        if ip is not None and url is None:
            self.by_addr(ip=ip)

    def by_name(self, url):
        ip = socket.gethostbyname(url)
        self.__eq__(ip=ip, url=url)


    def by_addr(self, ip):
        url = socket.gethostbyaddr(ip)[0]

        import requests
        try:
            req = requests.get(url="{}{}".format("http://www.", url))
            print(req.url)
            print(req.status_code)
        except Exception as e:
            print(e)

        # reverse_url = socket.gethostbyname(url)
        # self.__eq__(ip=ip, url=socket.gethostbyname(url))


    def __eq__(self, ip, url):

        if ip == url:
            self.state = True
        else:
            self.state = False




if __name__ == '__main__':

    targets = ["66.155.41.249",
               "66.155.40.250",
               "66.155.40.251",
               "66.155.40.252",
               "66.155.40.253",
               "66.155.40.254",
               "66.155.40.255"
               ]

    lookup = NSLookup()

    for i in targets:
        print(i)
        lookup.by_addr(ip=i)

