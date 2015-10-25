__author__ = 'N05F3R4TU'
__all__ = ["PathTraversal", "PathWindows"]

class PathTraversal(object):
    """
    https://www.owasp.org/index.php/Path_Traversal
    """

    def __init__(self):
        self.name = "Path Traversal Object"
        self.file = "strings.json"

    def paths(self):
        """
        Path Traversal
        """
        with open('strings.json', mode='rt', buffering=2000) as file:
            paths = [line.strip() for line in file.readlines()]
        return paths

class PathWindows:
    """
    Path Traversals for Windows Machines
    """
    def __init__(self):
        pass

    def paths(self):
        """
        C:/inetpub/wwwroot/global.asa
        C:\inetpub\wwwroot\global.asa
        C:/boot.ini
        C:\boot.ini
        D:\inetpub\wwwroot\global.asa
        D:/inetpub/wwwroot/global.asa
        :return:
        """
        pass