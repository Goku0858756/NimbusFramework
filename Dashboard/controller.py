__author__ = 'N05F3R4TU'
import sprint
import os

class DashboardController(object):

    def __init__(self, command=None, *args):
        self.name = "DashBoard Controller Object"
        self.task = args[0]
        self.full_path = os.path.dirname(os.path.realpath(__file__))
        self.server_file = "search.sh"

        if command in ["search"]:
            if self.task["start"]:
                self.elastic_search(task="start")
            if self.task["status"]:
                self.elastic_search(task="status")
            if self.task["stop"]:
                self.elastic_search(task="stop")
            if self.task["pid"]:
                self.elastic_search(task="pid")


    def elastic_search(self, task):

        if task in ["start", "stop"]:
            os.system("{}/{} {}".format(self.full_path, self.server_file, task))
        elif task in ["status", "pid"]:
            # print("Installing Elastic Search into Framework")
            os.system("{}/{} {}".format(self.full_path, self.server_file, task))
        else:
            print("I dont know what Task to Search for")

        # return "Elastic Search Controller"

    def kibana(self):
        return "Kiabana 4 Controller"

    def logstash(self):
        return "Logstash Controller"