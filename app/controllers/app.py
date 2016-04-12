import os
import sys
import random

from flask import Flask, flash, url_for, session
from flask import render_template
from flask import request
from random import randint

app_dir = os.path.abspath("..")
sys.path.insert(0, app_dir)

from models.restaurant_whole import Restaurant_whole
from models.customer import Customer
from models.menu_item import Menu_item

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
    filtered_restaurants = Restaurant_whole.query.filter(Restaurant.name.startswith(resname)).all()
    return render_template("search.html", restaurants=filtered_restaurants, res=True)


@app.route('/all_restaurants')
def all_restaurants():
    filtered_restaurants = Restaurant_whole.query.all()
    return render_template("all_restaurants.html", restaurants=filtered_restaurants)


@app.route('/adminrestaurantpage')
def adminrestaurantpage():
    filtered_restaurants_admin = Restaurant_whole.query.all()
    return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/deleterestaurant', methods=['POST'])
def deleterestaurant():
    id = request.form['Delete']
    record = Restaurant_whole.query.filter_by(_id=id).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
    filtered_restaurants_admin = Restaurant_whole.query.all()
    return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/addrestaurantpage')
def addrestaurantpage():
    return render_template("addrestaurantpage.html")


@app.route('/addrestaurant', methods=['POST'])
def addrestaurant():
    rest_name = request.form['inputRestName']
    owner_name = request.form['inputOwnerName']
    email = request.form['email']
    password = request.form['password']
    address = request.form['inputAddress']
    zipcode = request.form['inputZIP']
    rating = request.form['inputRating']
    record = Restaurant_whole(email, rest_name, owner_name, password, address, zipcode, rating)
    db.session.add(record)
    db.session.commit()
    filtered_restaurants_admin = Restaurant_whole.query.all()
    return render_template("adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/modifymenuitem')
def modifymenuitem():
    filtered_menu = Menu_item.query.all()
    return render_template("editmenuitempage.html", menu=filtered_menu)

@app.route('/addmenuitem', methods=['POST'])
def addmenuitem():
    name = request.form['inputName']
    res_id = random.randint(15,99)#After adding sessions this has to be referenced from the table
    description = request.form['description']
    cost = request.form['cost']
    rating = random.randint(1,5)
    record = Menu_item(res_id, name, description, float(cost), rating)
    db.session.add(record)
    db.session.commit()
    db.session.close()
    filtered_menu = Menu_item.query.all()
    return render_template("editmenuitempage.html", menu=filtered_menu)


@app.route('/addmenuitempage')
def addmenuitempage():
    return render_template("addmenuitempage.html")

@app.route('/deletemenuitem', methods=['POST'])
def deletemenuitem():
    modify_id = request.form['Modify'].split('_')
    record = []
    print modify_id[1]
    if modify_id[0]=="delete":
        record = Menu_item.query.filter_by(_id=modify_id[1]).all()
    else:
        record = Menu_item.query.filter_by(_id=modify_id[1]).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
        db.session.close()
    filtered_menu = Menu_item.query.all()
    return render_template("editmenuitempage.html", menu=filtered_menu)


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']
        user_type = request.form['login_type']
        if user_type == "customer":
            pass_real = Customer.query.filter(Customer.name == uname).first()
            if pass_real == password:
                error = 'Invalid Username/Password.'
            else:
                return render_template("user_homepage.html", user=uname)
        elif user_type == "rest_owner":
            pass_real = Restaurant_whole.query.filter(Customer.name == uname).first()
            if pass_real == password:
                error = 'Invalid Username/Password.'
            else:
                return render_template("user_homepage.html", user=uname)
        elif user_type == "admin":
            pass_real = Customer.query.filter(Customer.name == uname).first()
            if pass_real == password:
                error = 'Invalid Username/Password.'
            else:
                return render_template("user_homepage.html", user=uname)
        elif user_type == "delivery":
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

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template("sitemap.html", urls=links)
    # links is now a list of url, endpoint tuples

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