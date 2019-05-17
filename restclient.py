import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/todos/1')
response = json.loads(r.text[:200])
print(response)
