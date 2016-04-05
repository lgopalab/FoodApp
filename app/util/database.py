import json
import flask_sqlalchemy as falc
from flask import Flask

username = "root"
passwd = "123"
host = "localhost:3306"
db = "test2"
"""
with open("../../config/database.json") as props:
    params = json.loads(props.read())['params']
    username = params['username']
    passwd = params['password']
    host = params['host']
    db = params['db']
"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://%s:%s@%s/%s" % (username, passwd, host, db)

db = falc.SQLAlchemy(app)
