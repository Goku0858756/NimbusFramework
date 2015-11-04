__author__ = 'N05F3R4TU'

class Backup(object):
    """
    Backup the system
    """
    def __init__(self):
        pass

class Hibernate(object):
    """
    Hibernate ORM
    """
    def __init__(self):
        pass

class Encrypt(object):
    """
    Encrypt the System
    """
    def __init__(self):
        pass

class Hash(object):
    """
    Hashing the system
    """
    def __init__(self):
        pass

class System(object):
    """
    The System Management
    """
    def __init__(self):
        self.name = "System Management Object"
        self.id = id(self)

    def __str__(self):
        return str(self.__dict__)

    def start(self):
        """
        method to Start the system
        :return:
        """
        pass

    def stop(self):
        """
        Method to Stop the System (shutdown)
        :return:
        """
        pass

    def restart(self):
        """
        Method to Restart the system (activate helper, restart)
        :return:
        """
        pass