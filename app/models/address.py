from util.database import db
from util.database import db2

class Address(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	line1 = db.Column(db.String(40))
	apt = db.Column(db.String(1))
	line2 = db.Column(db.String(40))
	city = db.Column(db.String(12))
	state = db.Column(db.String(2))
	zipcode = db.Column(db.Integer)
	user_id = db.Column(db.Integer)


	def __init__(self, line1, apt, line2, city, state, zipcode, user_id):
		self.line1 = line1
		self.line2 = line2
		self.apt = apt
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.user_id = user_id

	def __repr__(self):
		return "%s,%s,%s,%s,%s,%s,%s" % (self.line1, self.apt, self.line2,
		                             self.city, self.state, self.zipcode, self._id)

class AddressTest(db2.Model):
	_id = db2.Column(db2.Integer, primary_key=True)
	line1 = db2.Column(db2.String(40))
	apt = db2.Column(db2.String(1))
	line2 = db2.Column(db2.String(40))
	city = db2.Column(db2.String(12))
	state = db2.Column(db2.String(2))
	zipcode = db2.Column(db2.Integer)
	user_id = db2.Column(db2.Integer)


	def __init__(self, line1, apt, line2, city, state, zipcode, user_id):
		self.line1 = line1
		self.line2 = line2
		self.apt = apt
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.user_id = user_id

	def __repr__(self):
		return "%s,%s,%s,%s,%s,%s,%s" % (self.line1, self.apt, self.line2,
		                             self.city, self.state, self.zipcode, self._id)
def main():
	db.create_all()
	db2.create_all()
