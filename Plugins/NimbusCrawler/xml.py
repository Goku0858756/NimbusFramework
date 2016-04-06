__author__ = 'N05F3R4TU'

import requests

# r = requests.get("http://mysmallwebpage.com/home/trackback/10500255")
r = requests.get("http://mysmallwebpage.com/process/RedirectN?url=http%3A%2F%2Fwww.ufetc.com")
print(r.text)

print(r.is_redirect)

# print(r.headers["content-type"])

print(r.encoding)
print(r.apparent_encoding)

print(r.status_code)




