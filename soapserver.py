import os
from flaskext.enterprise import Enterprise
from flask import Flask
from database import Database

db = Database("users.db")
#config Flask
app = Flask(__name__)

#config Flask Enterprise
enterprise = Enterprise(app)
String = enterprise._sp.String
Integer = enterprise._sp.Integer
Boolean = enterprise._sp.Boolean
Array = enterprise._scls.Array

class Service(enterprise.SOAPService):
    """Soap Service Class
    Attributes:
        __soap_target_namespace__ : namespace for soap service
        __soap_server_address__ : address of soap service
    """
    __soap_target_namespace__ = 'MyNS'
    __soap_server_address__ = '/soap'

    @enterprise.soap(Integer, _returns=String)
    def get_user(self, user):
        return db.read(user - 1)

    @enterprise.soap(String, Integer, _returns=String)
    def post_user(self, name, age):
        db.write('{ id: '+str(len(db.parsed_file))+', name: ' \
            + name.decode() + ', age: ' + str(age) + '}')
        return 'Succ'

    @enterprise.soap(String, _returns=String)
    def echo(self, mystring):
        return mystring

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
