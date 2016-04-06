__author__ = 'N05F3R4TU'
from nimbus import Nimbus

class AddTarget(Nimbus):

    def __init__(self, name=None, ip=None, url=None, dns=None, contract=None, pinned=None, note=None):
        import datetime
        super()
        self._id = id(self)

        self.target_id = "decimal(ip)"
        self.target_name = name
        self.target_ip = ip
        self.target_url = url
        self.target_contract = contract
        self.target_dns = dns
        self.target_note = note
        self.target_contract = contract # Temp
        self.target_pinned = pinned

        self.session_id = "ip + date + time"
        self.session_start = str(datetime.datetime.now())

        if self.target_ip is not None:
            from Plugins.IPConversion import controller
            self.target_id = controller.ip_to_int(self.target_ip)
            del controller

    def __str__(self):
        return str(self.__class__.__name__)

    def __del__(self):
        print(self.__class__.__name__, "Destroyed")
        return self

# if __name__ == '__main__':
#     a = AddTarget(ip='74.122.122.238')
#
#     for k, v in a.__dict__.items():
#         print("{} : {}".format(k, v))
#
#     # SHORTCUT CLiDL
#     # target add:ip:74.122.122.238 name:bol url:http://www.example.com