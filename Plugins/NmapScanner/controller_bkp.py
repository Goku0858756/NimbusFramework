__author__ = 'N05F3R4TU'
from subprocess import Popen, PIPE

def run():
    sudo_password = 'FrEaKi12'
    # command = 'nmap -Pn -sS -sV -A 217.149.143.62 -oX file-output.xml --reason --packet-trace'.split()
    # command = 'nmap -Pn -sS -sV -sU 217.149.143.62 -v -oX file-output2.xml'.split()
    command = 'nmap -Pn-sU 217.149.143.62 -v -oX file-output2.xml'.split()

    p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]
    print("_________ --- {}".format(sudo_prompt))





# class NmapScan(object):
#     """
#     Abstract Class to Integrate nMap into Nimbus Framework
#     """
#
#     def __init__(self, host_ip=None, host_name=None):
#         from subprocess import Popen, PIPE
#         self.name = "Nmap Scanner Object"
#         self.sudopsw = ""
#
#         if host_ip != None:
#             self.host_ip = host_ip
#         elif host_name != None:
#             self.host_name = host_name
#         elif host_ip != None and host_name != None:
#             print("Try again my friend. Both ip and Name is not posible! Try only IP")
#             # Convert and use only IP
#
#         self.sudo()
#         self.p = Popen(['sudo', '-S'] + self.command(), stdin=PIPE, stderr=PIPE, universal_newlines=True)
#
#     def scan(self):
#         """Scan run"""
#         sudo_prompt = self.p.communicate(self.sudo() + '\n')[1]
#
#
#     def sudo(self):
#         """What is the Sudo Password """
#         self.sudopswd = input("Sudo Password: ")
#         return
#
#     def ip_to_dec(self):
#         return "ip to decimal"
#
#     def command(self):
#         """
#
#         :param cmd:
#         :return:
#         """
#         return 'nmap -Pn-sU {} -v -oX file-output2.xml'.format(self.host_ip).split()


if __name__ == '__main__':
    # Check via decorator if Nmap is Installed on the system?
    # IF False print() error
    # IF True, go on with it
    # run()
    c = NmapScan(host_ip="217.149.143.62")
    c.scan()