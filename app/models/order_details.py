from util.database import db


class OrderDetails(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer)
	menu_item_id = db.Column(db.Integer)
	rest_id = db.Column(db.Integer)
	quantity = db.Column(db.Integer)


	def __init__(self, order_id, menu_item_id, rest_id, quantity):
		self.order_id = order_id
		self.menu_item_id = menu_item_id
		self.rest_id = rest_id
		self.quantity = quantity


	def __repr__(self):
		return "Order id: %d" % self.order_id
from util.database import db2


class OrderDetailsTest(db2.Model):
    _id = db2.Column(db2.Integer, primary_key=True)
    order_id = db2.Column(db2.Integer)
    menu_item_id = db2.Column(db2.Integer)
    rest_id = db2.Column(db2.Integer)
    quantity = db2.Column(db2.Integer)


    def __init__(self, order_id, menu_item_id, rest_id, quantity):
        self.order_id = order_id
        self.menu_item_id = menu_item_id
        self.rest_id = rest_id
        self.quantity = quantity


    def __repr__(self):
        return "Order id: %d" % self.order_id

def main():
	db.create_all()
	db2.create_all()
