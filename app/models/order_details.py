from app.util.database import db


class Order_Details(db.Model):
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
        return "Order ID:%s " % (self.order_id)