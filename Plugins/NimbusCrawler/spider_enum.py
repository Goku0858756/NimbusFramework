__author__ = 'N05F3R4TU'
__all__ = ["SpiderEnum"]

class SpiderEnum:
    """
    Spider Enumaration Object
    This object will check for attack vectors which can be invoked by the Spider Class
    @attacks; PathTraversal, HTTPMethodsAllowed, Fuzzing, BruteForce
    """
    def __init__(self):
        self.name = "Spider Function Object"

    def enum_path_traversal(self):
        """Enumerate; Directory Path Traversal"""
        pass

    def enum_http_methods(self):
        """Enumerate; Check what http methods are allowed"""
        pass

    def discover_admin(self):
        """Discover admin page"""
        pass

    def discover_virtual_hosts(self):
        """Discover; Check for virtual neighbour hosts"""
        pass

    def discover_geolocation(self):
        """Discover; Check or geolocation of server"""
        pass

    def attack_file_upload(self):
        """Attack; Try to upload shell files"""
        pass

    def attack_brute_force(self):
        """Attack; Brute Force default auth"""
        pass

    def attack_fuzzing(self):
        """Attack; Fuzz input fields"""
        pass
