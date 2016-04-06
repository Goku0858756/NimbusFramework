__author__ = 'N05F3R4TU'
import requests
import json

# TODO: Get List Proxy Resources
# TODO: nimbus --update-proxies
# TODO: nimbus <proxy-site-script>
# TODO: Parse ProxyList into dict
# TODO: Validate proxy's
# TODO: Best Proxy's Put into DB

URL = "http://httpbin.org/get"
AGENT = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36---"}
PAYLOAD = {'key1': 'value1', 'key2': 'value2'}
CONTENT = {'content-type': 'application/json'}


def random_proxy():
    import random

    proxylist = [
        'http://93.64.90.162:80',
        'http://117.136.234.4:80'
    ]
    # proxylist = {
    #     "http": "http://93.64.90.162:80"
    # }

    return random.choice(proxylist)

PROXIES = {
    "http": "http://117.136.234.4:80"
    # "https": "https://190.98.162.22:80"
}
proxiesDict = {
    # 'http' : "socks5://1.2.3.4:1080",
    'https' : "socks5://45.47.143.152:10200"
}


"""
    "http": "http://user:pass@10.10.1.10:3128/"
"""

# re = requests.get(url=URL, proxies=PROXIES)
# print(re.text)

"""
http://proxy-ip-list.com/download/txt-proxy-list.html
http://freeproxylist.org/en/free-proxy-list.htm
https://incloak.com/proxy-list/
http://txt.proxyspy.net/proxy.txt
http://proxypremium.blogspot.nl/2014/01/free-daily-proxy-list-txt-download.html
#### http://requestb.in/1lxp6k11?inspect
"""

if __name__ == '__main__':
    # print(type(PROXIES))
    # print(PROXIES)
    # print(type(random_proxy()))
    # print(random_proxy())


    for e, i in enumerate(range(1, 101)):
        # PROX = {"http": "{}".format(random_proxy())}
        # pr = "{}".format(PROX)
        # print(pr)

        re = requests.get(url=URL, proxies={"http": "{}".format(random_proxy())})
        print(re.text)