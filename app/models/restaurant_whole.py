from util.database import db

class RestaurantWhole(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    rest_name = db.Column(db.String(20))
    owner_name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    address = db.Column(db.String(30))
    zipcode = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, email, rest_name, owner_name, password, address, zipcode, rating):
        self.email = email
        self.rest_name = rest_name
        self.owner_name = owner_name
        self.password = password
        self.address = address
        self.zipcode = zipcode
        self.rating = rating

    def __repr__(self):
        return "%s %s" % (self.rest_name, self.email)

from util.database import db2

class RestaurantWholeTest(db2.Model):
    _id = db2.Column(db2.Integer, primary_key=True)
    email = db2.Column(db2.String(30))
    rest_name = db2.Column(db2.String(20))
    owner_name = db2.Column(db2.String(20))
    password = db2.Column(db2.String(20))
    address = db2.Column(db2.String(30))
    zipcode = db2.Column(db2.Integer)
    rating = db2.Column(db2.Integer)

    def __init__(self, email, rest_name, owner_name, password, address, zipcode, rating):
        self.email = email
        self.rest_name = rest_name
        self.owner_name = owner_name
        self.password = password
        self.address = address
        self.zipcode = zipcode
        self.rating = rating

    def __repr__(self):
        return "%s %s" % (self.rest_name, self.email)


def main():
    db.create_all()
    db2.create_all()