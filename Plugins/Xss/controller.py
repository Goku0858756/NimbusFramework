__author__ = 'N05F3R4TU'

class CrossSiteScripting(object):
    """
    URL: http://www.cefetra.nl/index.php?id=%22;%3E%3Cscript%3E
    URL: http://stackoverflow.com/questions/2661799/removing-x-powered-by
    URL: https://www.exploit-db.com/exploits/17318/
    URL: https://en.wikipedia.org/wiki/HTTP_header_injection
    URL: https://www.netsparker.com/web-vulnerability-scanner/vulnerability-security-checks-index/http-header-injection/
    """

    def __init__(self):
        self.name = "XSS Object"

    def extensions(self):
        return ".extension"
