__author__ = 'N05F3R4TU'

# def dqn_to_int(st):
def ip_to_int(ip):
    """
    Convert dotted quad notation to integer
    "127.0.0.1" => 2130706433
    """
    ip = ip.split(".")
    ###
    # That is not so elegant as 'for' cycle and
    # not extensible at all, but that works faster
    ###
    return int("%02x%02x%02x%02x" % (int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])),16)

def int_to_ip(ip):
    """
    Convert integer to dotted quad notation
    """
    ip = "%08x" % (ip)
    ###
    # The same issue as for `dqn_to_int()`
    ###
    return "%i.%i.%i.%i" % (int(ip[0:2],16),int(ip[2:4],16),int(ip[4:6],16),int(ip[6:8],16))

# if __name__ == '__main__':
#     print(ip_to_int("149.210.192.240"))
#     print(ip_to_int("149.210.192.241"))
#     print(ip_to_int("149.210.192.242"))
#     print(ip_to_int("149.210.192.243"))
#
#     print(int_to_ip(2513617136))
#     print(int_to_ip(2513617137))
#     print(int_to_ip(2513617138))
#     print(int_to_ip(2513617139))