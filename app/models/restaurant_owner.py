from util.database import db


class Restaurant_Owner(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    rest_id = db.Column(db.Integer)

    def __init__(self, email, username, password, rest_id):
        self.email = email
        self.username = username
        self.password = password
        self.rest_id = rest_id

    def __repr__(self):
        return "Restaurant ID:%s " % (self.rest_id)