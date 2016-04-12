from util.database import db


class Order_List(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    delivery_id = db.Column(db.Integer)

    def __init__(self, customer_id, delivery_id):
        self.customer_id = customer_id
        self.delivery_id = delivery_id

    def __repr__(self):
        return "User ID:%s Delivered by %s " % (self.customer_id, self.delivery_id)