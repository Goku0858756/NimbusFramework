__author__ = 'N05F3R4TU'

class DBConnect(object):
    """
    Database Persistent Connections Object
    """

    def __init__(self, host, port, username=None, password=None):
        self.name = "Database Connection Object"
        self.object_id = id(self)

        # Properties for this Connection Object
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        # These parameters should be given by the Object
        # Which calls this Object to create a OOP environment
        self.db_name = ""
        self.collections = []
        self.coll = ""

        # Global Connection variable for this Object
        self.mongo = ""
        self.db = self.handler()

    def connect(self, connect=True):
        from pymongo import MongoClient
        from pymongo.errors import ConnectionFailure
        import sys

        try:
            self.mongo = MongoClient(host=self.host, port=self.port, connect=connect)
        except ConnectionFailure as e:
            print("[ {} ]".format(self.__class__.__name__), str(e))
        finally:
            sys.exit(1)

    def handler(self):
        pass


class DBFunctions(object):
    """
    This Object Holds lots of Function that can be invoked by other Objects
    """
    def __init__(self):
        self.name = "Database Functions Object"

# if __name__ == '__main__':
#
#     d = DBConnect(host="localhost", port=27017)
#     d.connect()
#     d.handler = d.mongo["targets"]["targets"]
