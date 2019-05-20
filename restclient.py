import requests
import json
import timeit

r = requests.('http://0.0.0.0:8080/')
print(r.text[:200])
