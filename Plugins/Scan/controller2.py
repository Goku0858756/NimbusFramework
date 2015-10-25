__author__ = 'N05F3R4TU'
#!/usr/bin/env python
import nmap
from time import sleep

class NimbusScanner(nmap):

    def __init__(self):
        """
        Integrated Nmap Port Scanner
        :return:
        """
        self.scan = nmap.PortScanner()
        self.async_scan = nmap.PortScannerAsync()

        self.scan_id = 0
        self.scan_session = ""
        self.scan_template = ""
        self.scan_port = ""

    def new_scan(self, ip=None, port=None, sudo=False):
        return self.scan.scan(hosts=ip, ports=port, sudo=sudo)

    def command_line(self):
        return self.scan.command_line()

    def scan_info(self):
        return self.scan.scaninfo()

    def all_hosts(self):
        """
        get all hosts that were scanned
        :return:
        """
        return self.scan.all_hosts()

    def hosts_up(self):
        for host in self.scan.all_hosts():
            print("*"*40, "\nHosts Up")
            print('Host : %s (%s)' % (host, self.scan[host].hostname()))
            print('State : %s' % self.scan[host].state())

    def scanned_procotols(self):
        for p in self.scan[self.all_hosts()].all_protocols():
            print("*"*40, "\nProtocols")
            print('Protocol : %s' % p)

    # def host_port(self):
    #     lport = self.scan["host"]["protocol"].keys()
    #     lport.sort()
    #     print("*"*40, "\nPorts [ SORTED ]")
    #     for port in lport:
    #         print('port : %s\tstate : %s' % (port, self.[host][proto][port]['state']))

    def to_csv(self):
        return self.scan.csv()