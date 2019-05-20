import zeep
import timeit

wsdl = 'http://localhost:5000/soap?wsdl'
client = zeep.Client(wsdl=wsdl)
u = client.service.get_user(1)
print(u)
