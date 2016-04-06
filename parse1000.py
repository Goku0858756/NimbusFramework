import json
from pprint import pprint
from time import sleep
import base64


"""
HTTP/1.0 400 Bad Request
---------------
Server: AkamaiGHost
---------------
Mime-Version: 1.0
---------------
Content-Type: text/html
---------------
Content-Length: 193
---------------
Expires: Wed, 05 Nov 2014 15:10:38 GMT
---------------
Date: Wed, 05 Nov 2014 15:10:38 GMT
---------------
Connection: close
---------------
"""

"""
    HTTP/1.0  HTTP/1.1 200, 301, 400, 403

    302 Moved Temporarily

    400 Bad Request
    401 Unauthorized
    403
    404

    Server: ...
            AkamaiGHost
            Apache
            IIS
            NodeJS

    Server: Apache
    Server: Apache/2.2.15 (CentOS)
    Server: micro_httpd
    Server: Microsoft-HTTPAPI/2.0
    Server: SonicWALL
    Server: iGuard Embedded Web Server/3.6.8583S (LM520) SN:VK-2003-01D3-1508



"""

with open('1000linesv2.json', mode="r+") as file:

    for line in file.readlines():
        data = json.loads(line)
        print(data['host'])
        # print(base64.decode(data['data']))
        l = base64.b64decode(data['data'])

        # print(l.decode(encoding="ascii"))
        # print(l.decode(encoding='UTF-8'))
        sleep(1)


        for line in l.decode(encoding="ascii").splitlines():
            print(line)
            print("-"*15)
            # sleep(2)



        sleep(3)