__author__ = 'N05F3R4TU'

class Client(object):

    def __init__(self):
        self.name = "MongoDB Client Object"
        self.age = 18
        self.pid = id(self)

    def __str__(self):
        return str(self.__dict__)



if __name__ == '__main__':
    client = Client()

    print(client)

    client.age = 40


    print(client)