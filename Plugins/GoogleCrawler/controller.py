__author__ = 'N05F3R4TU'
from google import search

# s = [search(query="Microsoft Xbox One", stop=20)]

for url in search('"Breaking Code" WordPress blog', stop=20):
    print(type(url))

# for url in s:
#     print(url)