__author__ = 'N05F3R4TU'
__all__ = ['NSLookup']
import socket


class NSLookup:

    def __init__(self, ip=None, url=None):
        self.id = id(self)
        self.ip = ip
        self.url = url
        self.reverse_lookup = None

        if ip is not None and url is None:
            """if IP is given and No url"""
            self.by_addr(ip=ip)

        if ip is None and url is not None:
            """if URL is given and No IP"""
            self.by_name(url=url)

        if ip is not None and url is not None:
            """if IP is given AND URL is given"""
            self.by_name(url=url)
            self.by_addr(ip=ip)

    def by_name(self, url):
        self.ip = socket.gethostbyname(url)
        self.by_addr(ip=self.ip)
        # return socket.gethostbyname(url)

    def by_addr(self, ip):
        self.url = socket.gethostbyaddr(ip)[0]
        self.by_name(url=self.url)
        # return socket.gethostbyaddr(ip)

    def __eq__(self):
        if str(self.by_addr(ip=self.ip)[0]).lower() == str(self.url).lower():
            self.reverse_lookup = True
            return True
        else:
            self.reverse_lookup = False
            return False


if __name__ == '__main__':
    lookup = NSLookup(url="wordpress.org")
    print(lookup.ip)
    print(lookup.reverse_lookup)

    # print(lookup.by_name("budosportschiedam.nl"))
    # print(lookup.by_addr(ip="149.210.192.240"))

    # wordpress.org

    # url = lookup.by_name("wordpress.org")
    # print(url)
    #
    # name = lookup.by_addr(ip="66.155.40.249")
    # print(name[0])
    #
    # print(lookup.__eq__())

    # target1 = ["wordpress.org"]
    # target2 = ["66.155.40.249"]
    # target3 = {"wordpress.org": "66.155.40.249"}
