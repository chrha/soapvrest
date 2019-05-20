import zeep
import timeit

wsdl = 'http://localhost:5000/soap?wsdl'
client = zeep.Client(wsdl=wsdl)
start = timeit.timeit()
client.service.get_user(1)
end= timeit.timeit()
print(end - start)
