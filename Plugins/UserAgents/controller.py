__author__ = 'N05F3R4TU'
import json
from pprint import pprint

path = "strings.json"

with open(path) as useragent:
    data = json.load(useragent)

pprint(data)