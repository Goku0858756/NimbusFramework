__author__ = 'N05F3R4TU'
import datetime

class PluginObject(object):
    """
    Plugin Controller Object
    @Create a Abstract class to report When the Plugin is Created, PID, Thread. Name, Stats, Output
    @for Chaining purposes this abstract Object need to be as generic as possible
    """

    def __init__(self):
        self.name = "Plugin Name"

    def __str__(self):
        """
        For State (Hibernate) saving
        :return:
        """
        return str(self.__dict__)

    def __del__(self):
        """
        To keep track which component/Plugn is Done
        :return:
        """
        print(self.__class__.__name__, "Destructed at", datetime.datetime.now())
        return self

    def run(self):
        """
        For threading possiblities
        :return:
        """
        pass