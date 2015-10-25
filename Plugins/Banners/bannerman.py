__author__ = 'N05F3R4TU'
import socket

# host = "77.245.86.86 80"
# port = 80
#
# sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# sock.connect((host, port))


targets = {'google.com': '216.239.32.20',
           'msdn.microsoft.com': '157.56.148.19'
           }


def http_banner_grabber(ip, port=80, method="HEAD",
                        timeout=60, http_type="HTTP/1.1"):

    assert method in ['GET', 'HEAD']

    # @see: http://stackoverflow.com/q/246859/538284
    assert http_type in ['HTTP/0.9', "HTTP/1.0", 'HTTP/1.1']

    cr_lf = '\r\n'
    lf_lf = '\n\n'
    crlf_crlf = cr_lf + cr_lf
    res_sep = ''

    # how much read from buffer socket in every read
    rec_chunk = 4096
    s = socket.socket()
    s.settimeout(timeout)
    s.connect((ip, port))

    # the req_data is like 'HEAD HTTP/1.1 \r\n'
    req_data = "{} / {}{}".format(method, http_type, cr_lf)

    # if is a HTTP 1.1 protocol request,
    if http_type == "HTTP/1.1":

        # then we need to send Host header (we send ip instead of host here!)
        # adding host header to req_data like 'Host: google.com:80\r\n'
        req_data += 'Host: {}:{}{}'.format(ip, port, cr_lf)

        # set connection header to close for HTTP 1.1
        # adding connection header to req_data like 'Connection: close\r\n'
        req_data += "Connection: close{}".format(cr_lf)

    # headers join together with `\r\n` and ends with `\r\n\r\n`
    # adding '\r\n' to end of req_data
    req_data += cr_lf

    # the s.send() method may send only partial content.
    # so we used s.sendall()
    s.sendall(req_data.encode())
    res_data = b''

    # default maximum header response is different in web servers: 4k, 8k, 16k
    # @see: http://stackoverflow.com/a/8623061/538284
    # the s.recv(n) method may receive less than n bytes,
    # so we used it in while.
    while 1:
        try:
            chunk = s.recv(rec_chunk)
            res_data += chunk
        except socket.error:
            break
        if not chunk:
            break

    if res_data:
        # decode `res_data` after reading all content of data buffer
        res_data = res_data.decode()
    else:
        return '', ''

    # detect header and body separated that is '\r\n\r\n' or '\n\n'
    if crlf_crlf in res_data:
        res_sep = crlf_crlf
    elif lf_lf in res_data:
        res_sep = lf_lf

    # for under HTTP/1.0 request type for servers doesn't support it
    #  and servers send just send body without header !
    if res_sep not in [crlf_crlf, lf_lf] or res_data.startswith('<'):
        return '', res_data

    # split header and data section from
    # `HEADER\r\n\r\nBODY` response or `HEADER\n\nBODY` response
    content = res_data.split(res_sep)
    banner, body = "".join(content[:1]), "".join(content[1:])
    return banner, body

if __name__ == '__main__':

    # for domain, ip in targets.items():
    #     banner, body = http_banner_grabber(ip)
    #     print('*' * 24)
    #     print(domain, ip, 'HEAD HTTP/1.1')
    #     print(banner)

    for domain, ip in targets.items():
        banner, body = http_banner_grabber(ip, method="GET", http_type='HTTP/0.9')
        print('*' * 24)
        print(domain, ip, 'GET HTTP/0.9')
        print(banner)
