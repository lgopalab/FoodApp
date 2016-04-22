from util.database import db

class Menu_item(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	res_id = db.Column(db.Integer)
	name = db.Column(db.String(20))
	description = db.Column(db.String(50))
	cost = db.Column(db.Float)
	rating = db.Column(db.Integer)

	def __init__(self, res_id, name, description, cost, rating):
		self.res_id = res_id
		self.name = name
		self.description = description
		self.cost = cost
		self.rating = rating

	def __repr__(self):
		return "%s,%s,%s,%s" % (self.res_id, self.name, self.description, self.cost, self.rating)

if __name__ == "app.models.menu_item":
	db.create_all()