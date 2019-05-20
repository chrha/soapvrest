#!/usr/bin/env python
import web
from database import Database

db = Database("users.db")

urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/register', 'add_user'
)

app = web.application(urls, globals())

class list_users:
    def GET(self):
        return db.read_all()

class get_user:
    def GET(self, user):
        return db.read(int(user) - 1)

class add_user:
    def POST(self):
        i = web.input(_method='post')
        if i.name and i.age:
            db.write('{ id: '+ str(len(db.parsed_file)) + ', name: ' + i.name.decode() + ', age: ' + i.age.decode() + '}')
            return "Succ"
        return web.notfound("Sorry, invalid input.")

if __name__ == "__main__":
    app.run()
