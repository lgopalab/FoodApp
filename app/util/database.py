import json
import os
from flask import Flask
import flask_sqlalchemy as falc

with open("config/database.json") as props:
    params = json.loads(props.read())['params']
    username = params['username']
    passwd = params['password']
    host = params['host']
    db = params['db']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql://%s:%s@%s/%s" % (username, passwd, host, db)

db = falc.SQLAlchemy(app)


with open("config/testdb.json") as test_config:
	params = json.loads(test_config.read())['params']
	username = params["username"]
	passwd = params["password"]
	host = params["host"]
	database = params["db"]

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % (username, passwd, host, database)
db2 = falc.SQLAlchemy(app2)