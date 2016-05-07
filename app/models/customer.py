from util.database import db


class Customer(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    address = db.Column(db.String(1000))
    zipcode = db.Column(db.Integer)

    def __init__(self, email, name, password, address, zipcode):
        self.email = email
        self.name = name
        self.password = password
        self.address = address
        self.zipcode = zipcode

    def __repr__(self):
        return "name:%s, mail:%s" % (self.name,self.email)

from util.database import db2


class CustomerTest(db2.Model):
    _id = db2.Column(db2.Integer, primary_key=True)
    email = db2.Column(db2.String(40))
    name = db2.Column(db2.String(20))
    password = db2.Column(db2.String(20))
    address = db2.Column(db2.String(1000))
    zipcode = db2.Column(db2.Integer)

    def __init__(self, email, name, password, address, zipcode):
        self.email = email
        self.name = name
        self.password = password
        self.address = address
        self.zipcode = zipcode

    def __repr__(self):
        return "name:%s, mail:%s" % (self.name,self.email)

def main():
	db.create_all()
	db2.create_all()
