from util.database import db

class MenuItem(db.Model):
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

from util.database import db2

class MenuItemTest(db2.Model):
    _id = db2.Column(db2.Integer, primary_key=True)
    res_id = db2.Column(db2.Integer)
    name = db2.Column(db2.String(20))
    description = db2.Column(db2.String(50))
    cost = db2.Column(db2.Float)
    rating = db2.Column(db2.Integer)

    def __init__(self, res_id, name, description, cost, rating):
        self.res_id = res_id
        self.name = name
        self.description = description
        self.cost = cost
        self.rating = rating

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.res_id, self.name, self.description, self.cost, self.rating)

def main():
	db.create_all()
	db2.create_all()
