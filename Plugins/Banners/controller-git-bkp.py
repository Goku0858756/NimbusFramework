__author__ = 'N05F3R4TU'
import socket
from threading import Thread
from sys import platform

# Initialize
portlist = [21,22,25,80,110,443] # You can add more.

class bcolors:
    RED = '\033[91m'
    BOLD = '\033[1m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'


class BGrab():
    print(bcolors.RED + "\n #====" + bcolors.ENDC + bcolors.BOLD + "   SIMPLE BANNER GRABBING   " + bcolors.ENDC + bcolors.RED + "=============#" + bcolors.ENDC)
    print(bcolors.RED + " #==================" + bcolors.ENDC + bcolors.BOLD + "  v2 04/06/2015   " + bcolors.ENDC + bcolors.RED + "=========#" + bcolors.ENDC)
    print(bcolors.RED + " #=======================" + bcolors.ENDC + bcolors.BOLD + "   Hades.y2k   " + bcolors.ENDC + bcolors.RED + "=======#" + bcolors.ENDC)
    print(bcolors.RED + " #==== " + bcolors.ENDC + bcolors.BOLD + "www.github.com/Hadesy2k/banner-grab" + bcolors.ENDC + bcolors.RED + " ====#\n" + bcolors.ENDC)


    def __init__(self):
        self.enumerate()

    def first(self,ip):
        for x in range(0,129):
            for port in portlist:
                ip_address = ip + str(x)
                banner = self.Banner(ip_address, port)
                if banner:
                    print(bcolors.OKGREEN + "[+] " + bcolors.ENDC + bcolors.BOLD + ip_address + bcolors.ENDC + ':' + bcolors.BOLD + banner + bcolors.ENDC)

    def second(self,ip):
        for x in range(129,256):
            for port in portlist:
                ip_address = ip + str(x)
                banner = self.Banner(ip_address, port)
                if banner:
                    print(bcolors.OKGREEN + "[+] " + bcolors.ENDC + bcolors.BOLD + ip_address + bcolors.ENDC + ':' + bcolors.BOLD + banner + bcolors.ENDC)

    def Banner(self, ip, port):
        try:
            socket.setdefaulttimeout(2)
            soc = socket.socket()
            soc.connect((ip, port))
            banner = soc.recv(1024)
            return banner
        except:
            return

    def enumerate(self):
        # Initialize
        host = input(r"Enter the host name: ")
        print(bcolors.WARNING + '[+]' + bcolors.ENDC + bcolors.BOLD + " Engaging the Target" + bcolors.ENDC + "\n")
        init_ip = socket.gethostbyname(host)

        # This first-3 of ip method comes from pingsweep.py from the-c0d3r pynmap.
        octets = init_ip.split('.')
        # got 4 octets now
        # get first 3 octets, combine them with '.'
        # and iterate from 0 to 255 for the last octet
        ip = str(octets[0]+"."+octets[1]+"."+octets[2]+".")

        # Thread.start_new_thread(self.first(ip), ())
        # thread.start_new_thread(self.second(ip), ())

        thread1 = Thread(target=self.first, args=(ip,))
        thread2 = Thread(target=self.second, args=(ip,))

        thread1.start()
        thread2.start()

if __name__ == '__main__':
    # if 'linux' in platform:
    #     BGrab()
    # else:
    #     print('[!] This script works only in Linux.')
    #
    bg = BGrab()