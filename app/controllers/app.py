import os
import sys
import random
import time

from flask import Flask, flash, url_for, session
from flask import render_template
from flask import request
from random import randint

app_dir = os.path.abspath("..")
sys.path.insert(0, app_dir)

from models.restaurant_whole import Restaurant_whole
from models.admin import Admin
from models.customer import Customer
from models.menu_item import Menu_item

from util.database import db

app = Flask(__name__, template_folder='../templates', static_folder='../../public')
app.secret_key = 'some_secret'

#from tests.all_tests import Tests


@app.route("/")
@app.route("/home")
def home():
    print "home page"
    return render_template("home.html")


@app.route("/search")
def search_page():
    return render_template("search/search.html", restaurants=[], res=False)


@app.route("/user_display_menu", methods=['POST'])
def user_display_menu():
    print request.form['rest_id']
    filtered_menu = Menu_item.query.filter_by(_id=request.form['rest_id']).all()
    return render_template("user/displaymenupage.html", menu=filtered_menu)

@app.route("/search_restaurants", methods=['GET'])
def search_restaurants():
    resname = request.args.get('resname')
    filtered_restaurants = Restaurant_whole.query.filter(Restaurant_whole.rest_name.startswith(resname)).all()
    return render_template("search/search.html", restaurants=filtered_restaurants, res=True)


@app.route('/all_restaurants')
def all_restaurants():
    filtered_restaurants = Restaurant_whole.query.all()
    return render_template("search/all_restaurants.html", restaurants=filtered_restaurants)


@app.route('/adminrestaurantpage')
def adminrestaurantpage():
    filtered_restaurants_admin = Restaurant_whole.query.all()
    return render_template("admin/adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/deleterestaurant', methods=['POST'])
def deleterestaurant():
    id = request.form['Delete']
    record = Restaurant_whole.query.filter_by(_id=id).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
    filtered_restaurants_admin = Restaurant_whole.query.all()
    return render_template("admin/adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/addrestaurantpage')
def addrestaurantpage():
    return render_template("admin/addrestaurantpage.html")


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
    return render_template("admin/adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/modifymenu')
def modifymenu():
    print session['rest_id']
    filtered_menu = Menu_item.query.filter_by(_id=session['rest_id']).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


@app.route('/addmenuitem', methods=['POST'])
def addmenuitem():
    name = request.form['inputName']
    rest_id = session['rest_id']  # After adding sessions this has to be referenced from the table
    description = request.form['description']
    cost = request.form['cost']
    rating = random.randint(1, 5)
    record = Menu_item(rest_id, name, description, float(cost), rating)
    db.session.add(record)
    db.session.commit()
    filtered_menu = Menu_item.query.filter_by(res_id=rest_id).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


@app.route('/updatemenuitem', methods=['POST'])
def updatemenuitem():
    name = request.form['inputName']
    res_id = session['rest_id']
    menu_id = request.form['menu_id']
    description = request.form['description']
    cost = request.form['cost']
    print res_id, menu_id
    record = Menu_item.query.filter(Menu_item.res_id == res_id and Menu_item._id == menu_id).first()
    record.name = name
    record.description = description
    record.cost = cost
    db.session.commit()
    filtered_menu = Menu_item.query.filter_by(res_id=res_id).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


@app.route('/addmenuitempage')
def addmenuitempage():
    return render_template("res_owner/addmenuitempage.html")


@app.route('/deletemenuitem', methods=['POST'])
def deletemenuitem():
    modify_id = request.form['Modify'].split('_')
    record = []
    print modify_id[1]
    if modify_id[0] == "modify":
        record = Menu_item.query.filter_by(_id=modify_id[1]).all()
        return render_template("res_owner/modifymenuitempage.html", record=record)
    else:
        record = Menu_item.query.filter_by(_id=modify_id[1]).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
        db.session.close()
    filtered_menu = Menu_item.query.filter_by(res_id=session['rest_id']).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


# route for handling the login page logic
@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if not(session.get('logged_in')):
        print "inside after session condition"
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user_type = request.form['login_type']
            if email != "" and password != "":
                if user_type == "customer":  # Customer login validation
                    pass_real = Customer.query.filter_by(email=email).first()
                    if pass_real == None:
                        error = 'User Not found.'
                    elif pass_real.password == password:
                        session['logged_in'] = True
                        session['user_type'] = user_type
                        session['user_id'] = pass_real._id
                        return render_template("user/user_homepage.html", user=pass_real.name)
                    else:
                        error = 'Invalid Username/Password.'
                elif user_type == "rest_owner":  # Restaurant owner login validation
                    pass_real = Restaurant_whole.query.filter_by(email=email).first()
                    if pass_real == None:
                        error = "Restaurant owner not found."
                    elif pass_real.password == password:
                        session['logged_in'] = True
                        session['user_type'] = user_type
                        session['rest_id'] = pass_real._id
                        return render_template("res_owner/restaurant_owner_homepage.html", user=pass_real.owner_name)
                    else:
                        error = 'Invalid Username/Password.'
                else:  # Admin Validation
                    pass_real = Admin.query.filter_by(email=email).first()
                    if pass_real == None:
                        error = "Admin not found."
                    elif pass_real.password == password:
                        session['logged_in'] = True
                        session['user_type'] = user_type
                        session['admin_id'] = pass_real._id
                        return render_template("admin/admin_homepage.html", user=email)
                    else:
                        error = 'Invalid Username/Password.'
                return render_template("login/login.html", error=error)
            else:
                error="Both E-mail and Password are required."
                return render_template("login/login.html", error=error)
        else:
            print "in Else condition"
            return render_template("login/login.html", error=error)
    else:
        if session['user_type'] == "customer":
            user_id = int(session['user_id'])
            record = Customer.query.filter_by(_id=user_id).first()
            return render_template("user/user_homepage.html", user=record.name)
        elif session['user_type'] == "rest_owner":
            rest_id = int(session['rest_id'])
            record = Restaurant_whole.query.filter_by(_id=rest_id).first()
            print record
            return render_template("res_owner/restaurant_owner_homepage.html", user=record.owner_name)
        else:
            admin_id = int(session['admin_id'])
            record = Admin.query.filter_by(_id=admin_id).first()
            return render_template("admin/admin_homepage.html", user=record.email)


@app.route("/register")
def register():
    return render_template("register/register.html")


@app.route("/register_form", methods=['POST'])
def register_form():
    error = None
    user_type = request.form['user_type']
    if user_type == "customer":
        return render_template("register/register_customer.html",error=error)
    else:
        return render_template("register/register_res_owner.html",error=error)


@app.route("/complete_registration", methods=['POST'])
def complete_registration():
    error = None
    user_type = request.form['user_type']
    if user_type == "customer":
        user_name = request.form['name']
        email = request.form['email']
        address = " "
        password = request.form['password']
        cpassword = request.form['cpassword']
        zipcode = 0
        if password == cpassword:
            record = Customer(email, user_name, password, address, zipcode)
            db.session.add(record)
            db.session.commit()
            return render_template("register/register_success.html")
        else:
            error = "Password Doesn't match. Enter the values again"
            return render_template("register/register_customer.html", error=error)
    else:
        owner_name = request.form['owner_name']
        rest_name = request.form['rest_name']
        email = request.form['email']
        address = request.form['address']
        zipcode = request.form['zipcode']
        password = request.form['password']
        rating = random.randint(0, 5)
        record = Restaurant_whole(email, rest_name, owner_name, password, address, zipcode, rating)
        db.session.add(record)
        db.session.commit()
        return render_template("register/register_success.html", error=error)


@app.route("/logout")
def logout_user():
    session.pop('logged_in', None)
    return render_template("login/logout.html")


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


def main():
	#Tests.run_all()
	app.debug = True
	app.run(host='127.0.0.1')