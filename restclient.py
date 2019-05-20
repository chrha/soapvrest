import requests
import json
import timeit

payload = {'name': 'fahmi', 'age' : 45}
start = timeit.timeit()
r = requests.post('http://0.0.0.0:8080/register', data=payload)
end = timeit.timeit()
print(r.text[:200] + "\n")
print(end - start)
