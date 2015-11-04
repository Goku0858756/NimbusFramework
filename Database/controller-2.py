__author__ = 'N05F3R4TU'
from pymongo import MongoClient

class MongoServerController(object):
    """
    Server Controller
    """
    def __init__(self):
        self.mongo = MongoClient('localhost', 27017)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def start(self):
        pass

    def close(self):
        pass

class MongoClientController(object):
    """
    Client Controller
    """
    def __init__(self):
        self.mongo = MongoClient('localhost', 27017)

        # self.db = self.mongo['admin']
        self.dbs = self.mongo.database_names()

        self.mongo.close()


class MongoAdminController(object):

    def __init__(self):
        pass


def server():
    pass

def client_jobs():
    client = MongoClientController()
    print(client)


if __name__ == '__main__':
    # from queue import Queue
    # import multiprocessing
    #
    # q = multiprocessing.Queue()
    #
    # # Start a Job
    # thread_mongod, thread_server = multiprocessing.Process(target="", args=())
    print(client_jobs())