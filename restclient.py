import requests
import json
payload = {'name': 'stan', 'age': 35}
r = requests.post('http://0.0.0.0:8080/register',data = payload)
print(r.text[:200])
