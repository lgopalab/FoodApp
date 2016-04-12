from util.database import db

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
		return "%s,%s,%s,%s" % (self.name, self.address,self.zipcode, self.rating)
