__author__ = 'N05F3R4TU'
from nmap import PortScanner

#!/usr/bin/env python
from socket import *

if __name__ == '__main__':
    target = input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print('Starting scan on host ', targetIP)

    #scan reserved ports
    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print('Port %d: OPEN' % (i,))
        s.close()