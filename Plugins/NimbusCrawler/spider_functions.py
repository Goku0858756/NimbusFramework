__author__ = 'N05F3R4TU'
__all__ = ["SpiderFunction"]

class SpiderFunction:
    """
    Spider Function Object
    This object has al functions which can be invoked by the Spider Class
    Tags: This object is to tag URL
    """
    def __init__(self):
        self.name = "Spider Function Object"

    def recognize_xpath(self):
        """Tag; url as XPATH"""
        pass

    def recognize_form(self):
        """Tag; URL has form"""
        pass

    def recognize_extension(self):
        """Tag; check if URL has extension
        @extensions: .php, .asp, .html, .jsx, .js, .css
        """
        pass

    def recognize_php(self):
        """Tag; Check what PHP version is running"""
        pass

    def recognize_subdomain(self):
        """Tag; URL is subdomain
        @subdomain; admin.domain.com
        """

    def recognize_cdn(self):
        """Tag; check if URL is CDN"""
        pass

    def recognize_dork(self):
        """Tag; URL is a dork"""
        pass

    def reconstruct_url(self):
        """Reconstruct broken HREF"""
        pass
