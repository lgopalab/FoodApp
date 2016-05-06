from util.database import db


class Card_Details(db.Model):
    cardnum = db.Column(db.Integer, primary_key=True)
    cvv = db.Column(db.Integer)
    valid_thru =
    password = db.Column(db.String(20))


    def __init__(self, email, password):
        # type: (object, object) -> object
        self.email = email
        self.password = password


    def __repr__(self):
        return "name:%s, mail:%s" % (self.name.self.email)

def main():
    db.create_all()