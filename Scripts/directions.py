import requests
import pprint
import string
import re
import os
import json
import sys
import time


def getKey():
    f = open('../key.txt')
    key = f.read()
    return key

def getURL(source, destination):
    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='
    url += source
    url += "&destination="
    url += destination
    url += "&key="
    url += getKey()
    return string.replace(url, "\n", "")

def getDirections(source, destination):
    url = getURL(source, destination)
    print(url)
    r = requests.get(url)   
    obj = r.json()
    status = obj["status"]
    if status != "OK":
        return None

    return obj

s = "251 Mercer steet, New York NY"
d = "Empire State Building"

res = getDirections(s,d)
print(str(res))
