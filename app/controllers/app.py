import os
import sys

from flask import Flask, flash
from flask import render_template
from flask import request

app_dir = os.path.abspath("..")
sys.path.insert(0, app_dir)

from models.restaurant import Restaurant
from models.customer import Customer

from util.database import db

app = Flask(__name__, template_folder='../templates', static_folder='../../public')
app.secret_key = 'some_secret'


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


@app.route('/adminrestaurantpage')
def adminrestaurantpage():
	filtered_restaurants_admin = Restaurant.query.all()
	return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/deleterestaurant', methods=['POST'])
def deleterestaurant():
	id = request.form['Delete']
	record = Restaurant.query.filter_by(_id=id).all()
	for rec in record:
		db.session.delete(rec)
		db.session.commit()
	filtered_restaurants_admin = Restaurant.query.all()
	return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/addrestaurantpage')
def addrestaurantpage():
	return render_template("addrestaurantpage.html")


@app.route('/addrestaurant', methods=['POST'])
def addrestaurant():
	name = request.form['inputName']
	address = request.form['inputAddress']
	zipcode = request.form['inputZIP']
	rating = request.form['inputRating']
	record = Restaurant(name, address, zipcode, rating)
	db.session.add(record)
	db.session.commit()
	filtered_restaurants_admin = Restaurant.query.all()
	return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route("/add_menu_item")
def add_menu_item():
	return render_template("add_menu_item.html")


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		uname = request.form['username']
		password = request.form['password']
		pass_real = Customer.query.filter(Customer.name == uname).first()
		if pass_real == password:
			error = 'Invalid Username/Password.'
		else:
			return render_template("user_homepage.html", user=uname)
	return render_template('login.html', error=error)


@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/register_form", methods=['POST'])
def register_form():
	reg_type = request.form['reg_type']
	if reg_type == "customer":
		return render_template("register_customer.html")
	elif reg_type == "rest_owner":
		return render_template("register_res_owner.html")
	else:
		return render_template("register_del_boy.html")


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

@app.route("/logout")
def logout_user():
	return render_template("logout.html")


'''
@app.route("/add_menu", methods=['POST'])
def add_menu_item():
    item = request.form['myItems[]']
    price = request.form['myPrices[]']
    description= request.form['myDescriptions[]']
    print item, price, description
    record = Menu(item, price, description)
    db.session.add(record)
    db.session.commit()
    return render_template("menu.html")
'''


def main():
	app.debug = True
	app.run(host='127.0.0.1')