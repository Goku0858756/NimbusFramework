__author__ = 'N05F3R4TU'
from Modules import controller

class Scanner(controller.ModulesAbstract):
    """
    Abstract Scanner Object
    Calling to Child Objects to do Jobs
    @Scans to MongoDB with base64
    """
    def __init__(self):
        super(Scanner, self).__init__()
        self.name = "Scanner Concrete Object"

    def ip_scan(self):
        """
        Nmap Scan
        :return:
        """
        pass

    def port_scan(self):
        """
        NmapScan/ Hping
        :return:
        """
        pass

    def subdomain_scan(self):
        """
        KnockPy
        :return:
        """
        pass

    def socket_scan(self):
        """
        SockScan for Proxy
        :return:
        """
        pass

    def wp_scan(self):
        """
        Wordpress Scan
        :return:
        """
        pass

    def nslookup_scan(self):
        """
        Do a NSLookup
        :return:
        """
        pass

    def whois_scan(self):
        """
        Do a whois lookup
        :return:
        """
        pass

    def webserver_scan(self):
        """
        Determine if there is a webserver living on the host
        :return: -p80
        """
        pass
        # nmap -Pn -p80 -oX logs/pb-port80scan.xml -oG logs/pb-port80scan.gnmap 216.163.128.20/20

    def ip_to_int(self):
        from Plugins.IPConversion import controller
        print(controller.int_to_ip(2513617137))


# if __name__ == '__main__':
#     scanner = Scanner()
#     scanner.ip_to_int()