__author__ = 'N05F3R4TU'


class NTPAttack(object):
    """
    NTP protocol is een Time, Date protocol.
    Server & Monitoring. Send 1 Packet, Receive 600 Packets

    Sources:
     # https://github.com/vpnguy/ntpdos.git
     # https://github.com/limifly/ntpserver.git
     # https://github.com/sensepost/ntp_monlist.git
    """

    def __init__(self):
        self.attack_name = "NTP"

    def start_server(self):
        pass

    def start_client(self):
        pass
