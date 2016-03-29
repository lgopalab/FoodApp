import json

import flask_sqlalchemy as falc
from flask import Flask

username = ""
passwd = ""
host = ""
db = ""

with open('database.json') as props:
	params = json.loads(props.read())['params']
	username = params['username']
	passwd = params['password']
	host = params['host']
	db = params['db']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" %	(username,passwd,host, db)

db = falc.SQLAlchemy(app)

class Restaurant(db.Model):
	email = db.Column(db.String(20), primary_key=True)
	name = db.Column(db.String(20))
	password = db.Column(db.String(20))
	address = db.Column(db.String(30))
	zipcode = db.Column(db.Integer)


	def __init__(self, name, address, zipcode, rating):
		self.email = email
		self.name = name
		self.password = password
		self.address = address
		self.zipcode = zipcode