__author__ = 'N05F3R4TU'
import socket

class BannerGrabbing(object):

    def __init__(self):
        # targets takes only IP as parameters
        self.targets = []
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def grab(self, ip, port=80, method="HEAD", timeout=60, http_type="HTTP/1.1"):

        assert method in ['GET', 'HEAD']
        assert http_type in ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1']

        rn = '\r\n'
        nn = '\n\n'
        rnrn = rn + rn
        response_seperate = ''

        buffer_size = 4096
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip, port))

        # HEAD HTTP/1.1 \r\n
        request_head = "{} / {}{}".format(method, http_type, rn)
        if http_type == "HTTP/1.1":
            request_head += "Host: {}:{}{}".format(ip, port, rn)
            request_head += "Connection: close{}".format(rn)
        request_head += rn

        # Send Request
        sock.sendall(request_head.encode())

        """ [ RESPONSE ] """
        response_data = b''

        while True:
            try:
                chunk = sock.recv(buffer_size)
                response_data += chunk
            except socket.error:
                break

            if not chunk:
                break

        if response_data:
            response_data = response_data.decode()
        else:
            return "", ""

        if rnrn in response_data:
            response_seperate = rnrn
        elif nn in response_data:
            response_seperate = nn

        content = response_data.split(response_seperate)
        banner = "".join(content[:1])
        body = "".join(content[:1])

        return banner, body



if __name__ == '__main__':

    ip = "185.14.169.113"
    b = BannerGrabbing()

    banner, body = b.grab(socket.gethostbyname("www.-----.nl"))
    # print(body)

    for l in banner.splitlines():

        if "Server" in l:
            print(l)
        elif "Content-Type" in l:
            print(l)
        elif "X-Powered-By" in l:
            print(l)
