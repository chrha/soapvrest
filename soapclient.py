import zeep
wsdl = 'http://localhost:5000/soap?wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.echo('input2'))
