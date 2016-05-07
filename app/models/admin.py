from util.database import db

class Admin(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(20))


    def __init__(self, email, password):
        # type: (object, object) -> object
        self.email = email
        self.password = password


    def __repr__(self):
        return "mail:%s" % self.email

from util.database import db2

class AdminTest(db2.Model):
    _id = db2.Column(db2.Integer, primary_key=True)
    email = db2.Column(db.String(40))
    password = db2.Column(db.String(20))


    def __init__(self, email, password):
        # type: (object, object) -> object
        self.email = email
        self.password = password


    def __repr__(self):
        return "mail:%s" % self.email


def main():
	db.create_all()
	db2.create_all()