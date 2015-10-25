__author__ = 'N05F3R4TU'
import nmap
from time import sleep

host = '217.149.143.62'
nm = nmap.PortScanner() # instantiate nmap.PortScanner object
# print(nm.scan('149.210.192.240', '0-9000')) # scan host 127.0.0.1, ports from 22 to 443
#
# print("*" * 40, "\nCommandLine:")
# sleep(4)
# print(nm.command_line()) # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
#
# # print("*" * 40, "\nScaninfo:")
# # sleep(4)
# # print(nm.scaninfo())# get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
#
# # print("*" * 40, "\nAll Hosts:")
# # sleep(4)
# # print(nm.all_hosts()) # get all hosts that were scanned
#
# for host in nm.all_hosts():
#     print("*"*40, "\nHosts Up")
#     print('Host : %s (%s)' % (host, nm[host].hostname()))
#     print('State : %s' % nm[host].state())
#
# for proto in nm[host].all_protocols():
#     print("*"*40, "\nProtocols")
#     print('Protocol : %s' % proto)
#
# lport = nm[host][proto].keys()
# lport.sort()
# print("*"*40, "\nPorts [ SORTED ]")
# for port in lport:
#     print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
#
# print("*"*40, "\nPrint to CSV")
# sleep(4)
# # print result as CSV
# print(nm.csv())

