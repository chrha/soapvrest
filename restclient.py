import requests

r = requests.get('http://0.0.0.0:8080/1')
print(r.text[:200])
