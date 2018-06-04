import random

print(random.randint(0,5))
print(random.randint(0,5))
print(random.randint(0,5))
print(random.randint(0,5))
print(random.randint(0,5))
print(random.random())

import time

print(time.localtime())

import urllib.request
response = urllib.request.urlopen("http://www.naver.com")

for i in response:
    print(i)
