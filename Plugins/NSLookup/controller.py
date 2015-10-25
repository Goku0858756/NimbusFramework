__author__ = 'N05F3R4TU'
__all__ = ['NSLookup']
import socket


class NSLookup:

    # def __init__(self, url=None, ip=None):
    #     # self.name = url
    #     # self.ip = ip
    #
    #     # if self.name is not None:
    #     #    self.by_name()
    #     #
    #     # if self.ip is not None:
    #     #     self.by_addr(ip=self.ip)


    def by_name(self, url):
        print(socket.gethostbyname(url))
        # return socket.gethostbyname(host=url)

    def by_addr(self, ip):
        print(socket.gethostbyaddr(ip))
        # return socket.gethostbyaddr(ip)





if __name__ == '__main__':
    lookup = NSLookup()

    print(lookup.by_name("http://www.budosportschiedam.nl"))
    # print(lookup.by_addr(ip="149.210.192.240"))
