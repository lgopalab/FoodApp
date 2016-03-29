import flask_sqlalchemy as falc
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://localhost:3306/test"
db = falc.SQLAlchemy(app)

print db

class Restaurant(db.Model):
	_email = db.Column(db.String(20), primary_key=True)
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
