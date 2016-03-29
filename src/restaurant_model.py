from flask import Flask
import flask_sqlalchemy as falc
import json

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
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" %	(username,
																																 passwd,
																																 host, db)

db = falc.SQLAlchemy(app)

class Restaurant(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	address = db.Column(db.String(30))
	zipcode = db.Column(db.Integer)
	rating = db.Column(db.Integer)

	def __init__(self, name, address, zipcode, rating):
		self.name = name
		self.address = address
		self.zipcode = zipcode
		self.rating = rating

	def __repr__(self):
		return "%s at %s, %s - rating: %s" % (self.name, self.address, 
																					self.zipcode, self.rating)