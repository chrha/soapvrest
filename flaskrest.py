from flask import Flask, flash, redirect, render_template, request, session, abort
from database import Database
app = Flask(__name__)
db = Database("users.db")

@app.route("/<int:user>")
def get_user(user):
    return db.read(int(user))

@app.route("/register", methods=['POST'])
def register_user():
    data = request.form
    db.write('{ id: '+ str(len(db.parsed_file)) + ', name: ' + data['name'].decode() + ', age: ' + data['age'].decode() + '}')
    return 'Succ'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
