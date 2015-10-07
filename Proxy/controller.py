__author__ = 'N05F3R4TU'
import requests


# TODO: Get List Proxy Resources
# TODO: nimbus --update-proxies
# TODO: nimbus <proxy-site-script>
# TODO: Parse ProxyList into dict
# TODO: Validate proxy's
# TODO: Best Proxy's Put into DB

URL = "http://httpbin.org/get"
AGENT = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
PAYLOAD = {'key1': 'value1', 'key2': 'value2'}
CONTENT = {'content-type': 'application/json'}

PROXIES = { "http": "68.234.200.187:8080"}


"""
    "http": "http://user:pass@10.10.1.10:3128/"
"""

re = requests.get(url=URL, proxies=PROXIES)
print(re.text)