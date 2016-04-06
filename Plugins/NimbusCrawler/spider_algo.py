__author__ = 'N05F3R4TU'
__all__ = ["SpiderAlgo"]

class SpiderAlgo(object):
    """
    Default Algorithm Object which can be replaced by input of user with a file.yml
    """
    def __init__(self):
        self.name = "Spider Algorith Object"

    def default(self):
        """
        :return dict with sequence of function to be performed by the crawler
        """
        pass

    def algorithm(self):
        """
        This is a Blue-Print or Algorithm if you may for the Spider to do the Web-Audit
        :return:
        """
        try:
            # First verify url is working by doing a Request and get_status 200
            if self.host_alive(url=self.spider_url) != 200:
                assert "Host is not Alive. Please Double Check"

            # Parse the Url into Peaces
            # Check HTTP or HTTPS
                # if HTTPS then; cert_validation()
            self.url_analysis(url=self.spider_url)
            print("done: url analysis")

            # if url; then; Get url_to_ip && ip_to_decimal
            # then;
            # Connect to the Target-Object in the Database and Update the Crawl-Status
            # <code> [ NimbusDNS ]

            # Maak een Object() aan direct met de Database en Target
            self.create_object()

            # Webhost Enum; [ Mother Function ]
            # by using plugins
            self.webhost_discover_mode()

            # First Check if site is a known CMS or Framework
            self.framework_discover_mode()

            # Secondly do a URL-link crawl
                # import settings
                # and GO
            self.crawl_mode()

        except Exception as e:
            print("[ ALGORITHM_EXCEPTION ]", str(e))
