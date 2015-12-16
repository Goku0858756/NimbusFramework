__author__ = 'N05F3R4TU'
import requests
import re
import json

# def clean_json(string):
#     string = re.sub(",[ \t\r\n]+}", "}", string)
#     string = re.sub(",[ \t\r\n]+\]", "]", string)
#     return string

def delete(url):
    print(requests.delete(url).text)

def post(url, payload):
    requests.post(url=url, json=payload)

# payload = {
#     "user" : "sdfsdfsdf dsfsdfsdfsd",
#     "post_date" : "2009-11-15T14:12:12",
#     "message" : "trying out Elasticsearch"
# }

# print(requests.post(url=url, json=payload))

p = {"host": "23.204.93.33", "data": "SFRUUC8xLjAgNDAwIEJhZCBSZXF1ZXN0DQpTZXJ2ZXI6IEFrYW1haUdIb3N0DQpNaW1lLVZlcnNpb246IDEuMA0KQ29udGVudC1UeXBlOiB0ZXh0L2h0bWwNCkNvbnRlbnQtTGVuZ3RoOiAxOTMNCkV4cGlyZXM6IFdlZCwgMDUgTm92IDIwMTQgMTU6MTA6MzggR01UDQpEYXRlOiBXZWQsIDA1IE5vdiAyMDE0IDE1OjEwOjM4IEdNVA0KQ29ubmVjdGlvbjogY2xvc2UNCg0KPEhUTUw+PEhFQUQ+CjxUSVRMRT5JbnZhbGlkIFVSTDwvVElUTEU+CjwvSEVBRD48Qk9EWT4KPEgxPkludmFsaWQgVVJMPC9IMT4KVGhlIHJlcXVlc3RlZCBVUkwgIiYjNDc7IiwgaXMgaW52YWxpZC48cD4KUmVmZXJlbmNlJiMzMjsmIzM1OzkmIzQ2OzFmZTllZjNmJiM0NjsxNDE1MjAwMjM4JiM0NjszYjUzZDExCjwvQk9EWT48L0hUTUw+Cg==", "port": 80}
post("http://localhost:9200/scanio/scan/0/", p)

e = 1

with open('new1000.json', mode="r", buffering=2000) as file:
    for i in file.readlines():

        url = '{}{}/'.format("http://localhost:9200/scanio/scan/", e)
        requests.post(url, i)
        e +=1
        print(e)


# with open('new1000.json', mode="w+") as new:
#
#     with open('1000lines.json', mode="r", buffering=2000) as file:
#
#         for i in file.readlines():
#             new.write(i.replace('},', "}"))
#
