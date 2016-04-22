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
        return "name:%s, mail:%s" % (self.name.self.email)

if __name__ == "app.models.admin":
	db.create_all()