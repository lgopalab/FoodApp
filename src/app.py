from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from restaurant_model import Restaurant
from customer_model import Customer

from database import db

app = Flask(__name__)


@app.route('/')
def home():
    print "home page"
    return render_template("home.html")


@app.route("/search")
def search_page():
    return render_template("search.html", restaurants=[], res=False)


@app.route("/search_restaurants", methods=['GET'])
def search_restaurants():
    resname = request.args.get('resname')
    filtered_restaurants = Restaurant.query.filter(Restaurant.name.startswith(resname)).all()
    return render_template("search.html", restaurants=filtered_restaurants, res=True)


@app.route('/all_restaurants')
def all_restaurants():
    filtered_restaurants = Restaurant.query.all()
    return render_template("all_restaurants.html", restaurants=filtered_restaurants)


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']
        pass_real = Customer.query.filter(Customer.name==uname).first()
        if pass_real == password:
            error = 'Invalid Username/Password.'
        else:
            return render_template("user_homepage.html", user=uname)
    return render_template('login.html', error=error)


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/complete_registration", methods=['POST'])
def complete_registration():
    user_name = request.form['name']
    email = request.form['email']
    address = ""
    password = request.form['password']
    zipcode = 0
    print email, user_name, password, address, zipcode

    record = Customer(email, user_name, password, address, zipcode)
    db.session.add(record)
    db.session.commit()
    return render_template("register_success.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
