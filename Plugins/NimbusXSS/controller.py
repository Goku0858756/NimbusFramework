__author__ = 'N05F3R4TU'
import requests
from bs4 import BeautifulSoup



# class CrossSiteScripting(object):
#     """
#     URL: http://www.cefetra.nl/index.php?id=%22;%3E%3Cscript%3E
#     URL: http://stackoverflow.com/questions/2661799/removing-x-powered-by
#     URL: https://www.exploit-db.com/exploits/17318/
#     URL: https://en.wikipedia.org/wiki/HTTP_header_injection
#     URL: https://www.netsparker.com/web-vulnerability-scanner/vulnerability-security-checks-index/http-header-injection/
#     """
#
#     def __init__(self):
#         self.name = "XSS Object"


def smoke_test(url=None, payload=None, headers=None):
    req = requests.post(url=url, headers=headers)
    # print(req.is_redirect)
    # print(req.status_code)
    # print(req.headers)

    soup = BeautifulSoup(req.text)
    print("-"*40)
    print("FIND PAYLOAD: {}".format(req.text.find(payload)))
    print(req.url)

    payload_start = req.text.find(payload)
    # print(req.text[payload_start-1])

    # print(soup.find_all(name=payload))
    print("-"*40)

    return req.text



def main():
    # URL = 'http://httpbin.org/get'
    # URL = 'http://public-firing-range.appspot.com/reflected/parameter/title?q=asasasas'
    PAYLOAD = '<'
    URL = 'http://www.gamemania.nl/Resources/Shared/Scripts/jquery/jquery.hoverIntent.min.js?cdv={}'.format(PAYLOAD)
    UA = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36'}

    print(smoke_test(url=URL, headers=UA, payload=PAYLOAD))


if __name__ == '__main__':
    main()