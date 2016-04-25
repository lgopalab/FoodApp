from util.database import db

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

if __name__ == "app.models.address":
	db.create_all()