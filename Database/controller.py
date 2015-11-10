__author__ = 'N05F3R4TU'

def sprint(string):
    print("nimbus \> %s" % string)


class DatabaseController(object):
    """
    This Database Controller Object is used to Manage MongoDB from within the Framework
    """
    def __init__(self, *args):
        import os
        """
        {'dbs': False, 'status': False, 'pid': False, 'start': True, 'stop': False, 'add': False}
        """
        self.name = "MongoDB Manage Object"
        self.args = args[0]
        self.full_path = os.path.dirname(os.path.realpath(__file__))
        self.server_file = "server.sh"

        if self.args['start']:
            """
            IF STATUS [DOWN]; then
            """
            self.mongo("start")


        if self.args['stop']:
            """
            IF STATUS [UP]; then
            """
            self.mongo("stop")

        if self.args['status']:
            self.mongo("status")

        # self.status()

    # def status(self):
    #     import os
    #     os.system("pgrep mongod > pid.pid")

    def mongo(self, *args):
        import subprocess, shlex
        import os
        os.system("{}/{} {}".format(self.full_path, self.server_file, args[0]))
        # print(os.path.dirname(os.path.realpath(__file__)))
        # subprocess.call(shlex.split("{}/{} {}".format(self.full_path, self.server_file, args[0])))