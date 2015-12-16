__author__ = 'N05F3R4TU'
import nmap

class NmapScan(object):

    def __init__(self):
        self.name = "Nmap Scan Object"

    def arguments(self):
        pass



if __name__ == '__main__':
    pass

    # PIPY = "https://pypi.python.org/pypi/python-nmap"

    # target information
    NAME = 'sirolf.com'
    IP = '149.210.192.240'
    PORT = "21"
    PORTS = "21-443"

    # instantiate nmap.PortScanner object
    nm = nmap.PortScanner()

    # scan host IP, ports from 22 to 443
    print(nm.scan(IP, PORTS))

    # print("[ COMMAND.LINE ]", nm.command_line())                  # get command line used for the scan : nmap -oX - -p 22-443 IP
    # print("[ ALL.INFO ]", nm.scaninfo())                       # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
    # # print("[ ALL.HOSTS ]", nm.all_hosts())                     # get all hosts that were scanned
    # # print("[ HOSTNAME ]", nm[IP].hostname())          # get one hostname for host IP, usualy the user record
    # # print("[ HOSTNAMES ]", nm[IP].hostnames())         # get list of hostnames for host IP as a list of dict
    # # [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
    # print(nm[IP].hostname())          # get hostname for host IP
    # print("[ STATE ]", nm[IP].state())             # get state of host IP (up|down|unknown|skipped)
    # print("[ ALL.PROTOCOLS ]", nm[IP].all_protocols())     # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
    # print("[ TCP.PORTS ]", nm[IP]['tcp'].keys() )      # get all ports for tcp protocol
    # print(nm[IP].all_tcp())           # get all ports for tcp protocol (sorted version)
    # # nm[IP].all_udp()           # get all ports for udp protocol (sorted version)
    # print("[ ALL.IPs ]", nm[IP].all_ip())           # get all ports for ip protocol (sorted version)
    # # nm[IP].all_sctp()          # get all ports for sctp protocol (sorted version)
    # print("[ HAS.TCP ]", nm[IP].has_tcp(22))        # is there any information for port 22/tcp on host IP
    # nm.ha
    # print("[ INFO.PORT ]", nm[IP]['tcp'][22])         # get infos about port 22 in tcp on host IP
    # # nm[IP].tcp(22)             # get infos about port 22 in tcp on host IP
    # print("[ STATE.PORT ]", nm[IP]['tcp'][80]['state']) # get state of port 22/tcp on host IP (open
    # print("[ TO.CSV ]", nm.csv())
