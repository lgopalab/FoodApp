from app.util.database import db


class Order_List(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)

    def __init__(self, user_id):
        self.customer_id = customer_id

    def __repr__(self):
        return "User ID:%s " % (self.customer_id)