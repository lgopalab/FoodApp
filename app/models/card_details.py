from util.database import db


class CardDetails(db.Model):
    cardnum = db.Column(db.Integer, primary_key=True)
    cvv = db.Column(db.Integer)
    password = db.Column(db.String(20))

    def __init__(self, email, password):
        # type: (object, object) -> object
        self.email = email
        self.password = password


    def __repr__(self):
        return "name:%s, mail:%s" % (self.name.self.email)

from util.database import db2


class CardDetailsTest(db2.Model):
    cardnum = db2.Column(db2.Integer, primary_key=True)
    cvv = db2.Column(db2.Integer)
    password = db2.Column(db2.String(20))

    def __init__(self, email, password):
        # type: (object, object) -> object
        self.email = email
        self.password = password


    def __repr__(self):
        return "name:%s, mail:%s" % (self.name.self.email)


def main():
    db.create_all()
    db2.create_all()