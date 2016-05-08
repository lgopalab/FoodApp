import os
import sys
import random
import time
import itertools

from flask import Flask, flash, url_for, session
from flask import render_template
from flask import request
from random import randint
from sqlalchemy import desc

app_dir = os.path.abspath("..")
sys.path.insert(0, app_dir)

from models.restaurant_whole import RestaurantWhole
from models.admin import Admin
from models.customer import Customer
from models.menu_item import MenuItem
from models.address import Address
from models.order_list import OrderList
from models.order_details import OrderDetails

from util.database import db

app = Flask(__name__, template_folder='../templates', static_folder='../../public')
app.secret_key = 'some_secret'

from tests.orm.orm_tests import ORMTests
from tests.controller.controller_tests import ControllerTests

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
    filtered_menu = MenuItem.query.filter_by(res_id=request.form['rest_id']).all()
    return render_template("user/displaymenupage.html", menu=filtered_menu)

@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    item_id=request.form['menu_item_id']
    quantity = request.form['quantity']
    if item_id in session['menu_item_list']:
        index = session['menu_item_list'].index(item_id)
        temp_list = session['quantity_list']
        temp_list[index]=quantity
        session['quantity_list'] = temp_list
        rest_name_list = []
        menu_item_name_list = []
        menu_item_cost_list = []
        for i in session['menu_item_list']:
            rest_id = MenuItem.query.filter_by(_id=i).first()
            menu_item_name_list.append(rest_id.name)
            menu_item_cost_list.append(rest_id.cost)
            rest_name = RestaurantWhole.query.filter_by(_id=rest_id.res_id).first()
            rest_name_list.append(rest_name.rest_name)
        total = 0.0
        for i,j in zip(session['quantity_list'],menu_item_cost_list):
            total += float(j) * int(i)
        session["order_cost"] = total
        return render_template("user/displaycart.html",item_quantity_list=zip(session['menu_item_list'], session['quantity_list'],rest_name_list, menu_item_name_list,menu_item_cost_list),cost=session["order_cost"])
    else:
        session['menu_item_list'].append(item_id)
        session['quantity_list'].append(quantity)
        rest_name_list = []
        menu_item_name_list = []
        menu_item_cost_list = []
        for i in session['menu_item_list']:
            rest_id = MenuItem.query.filter_by(_id=i).first()
            menu_item_name_list.append(rest_id.name)
            menu_item_cost_list.append(rest_id.cost)
            rest_name = RestaurantWhole.query.filter_by(_id = rest_id.res_id ).first()
            rest_name_list.append(rest_name.rest_name)
            print rest_name_list
        total = 0.0
        for i, j in zip(session['quantity_list'], menu_item_cost_list):
            total += float(j) * int(i)
        session["order_cost"] = total
        return render_template("user/displaycart.html",item_quantity_list=zip(session['menu_item_list'],session['quantity_list'],rest_name_list,menu_item_name_list,menu_item_cost_list),cost=session["order_cost"])

@app.route("/display_cart")
def display_cart():
    rest_name_list = []
    menu_item_name_list = []
    menu_item_cost_list = []
    if 'menu_item_list' in session:
        for i in session['menu_item_list']:
            rest_id = MenuItem.query.filter_by(_id=i).first()
            menu_item_name_list.append(rest_id.name)
            menu_item_cost_list.append(rest_id.cost)
            rest_name = RestaurantWhole.query.filter_by(_id=rest_id.res_id).first()
            rest_name_list.append(rest_name.rest_name)
        total = 0.0
        for i,j in zip(session['quantity_list'],menu_item_cost_list):
            total += float(j) * int(i)
        session["order_cost"] = total
        return render_template("user/displaycart.html",item_quantity_list=zip(session['menu_item_list'], session['quantity_list'],rest_name_list,menu_item_name_list,menu_item_cost_list),cost=session["order_cost"])
    else:
        return render_template("user/displayemptycart.html")

@app.route("/post_order_address", methods=['POST'])
def post_order_address():
    if session['logged_in']:
        addresses = Address.query.filter_by(user_id=session['user_id']).all()
        return render_template("user/post_order_address.html", addresses=addresses)

@app.route("/post_order", methods=['POST'])
def post_order():
    if session['logged_in']:
        address_id = request.form["address_id"]
        db.session.add(OrderList(session['user_id'],address_id))
        db.session.commit()
        order = OrderList.query.filter_by(customer_id=session['user_id']).order_by(OrderList._id.desc()).first()
        for i,j in zip(session['menu_item_list'],session['quantity_list']):
            db.session.add(OrderDetails(order._id,i,j))
            db.session.commit()
        addresses = Address.query.filter_by(user_id=session['user_id']).all()
        return render_template("user/post_order_address.html", addresses=addresses)

@app.route("/search_restaurants", methods=['GET'])
def search_restaurants():
    resname = request.args.get('resname')
    filtered_restaurants = RestaurantWhole.query.filter(RestaurantWhole.rest_name.startswith(resname)).all()
    return render_template("search/search.html", restaurants=filtered_restaurants, res=True)


@app.route('/all_restaurants')
def all_restaurants():
    filtered_restaurants = RestaurantWhole.query.all()
    return render_template("search/all_restaurants.html", restaurants=filtered_restaurants)


@app.route('/adminrestaurantpage')
def adminrestaurantpage():
    filtered_restaurants_admin = RestaurantWhole.query.all()
    return render_template("admin/adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/deleterestaurant', methods=['POST'])
def deleterestaurant():
    id = request.form['Delete']
    record = RestaurantWhole.query.filter_by(_id=id).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
    filtered_restaurants_admin = RestaurantWhole.query.all()
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
    record = RestaurantWhole(email, rest_name, owner_name, password, address, zipcode, rating)
    db.session.add(record)
    db.session.commit()
    filtered_restaurants_admin = RestaurantWhole.query.all()
    return render_template("admin/adminrestaurant.html", restaurants=filtered_restaurants_admin)


@app.route('/modifymenu')
def modifymenu():
    print session['rest_id']
    filtered_menu = MenuItem.query.filter_by(_id=session['rest_id']).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


@app.route('/addmenuitem', methods=['POST'])
def addmenuitem():
    name = request.form['inputName']
    rest_id = session['rest_id']  # After adding sessions this has to be referenced from the table
    description = request.form['description']
    cost = request.form['cost']
    rating = random.randint(1, 5)
    record = MenuItem(rest_id, name, description, float(cost), rating)
    db.session.add(record)
    db.session.commit()
    filtered_menu = MenuItem.query.filter_by(res_id=rest_id).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


@app.route('/updatemenuitem', methods=['POST'])
def updatemenuitem():
    name = request.form['inputName']
    res_id = session['rest_id']
    menu_id = request.form['menu_id']
    description = request.form['description']
    cost = request.form['cost']
    print res_id, menu_id
    record = MenuItem.query.filter(MenuItem.res_id == res_id and MenuItem._id == menu_id).first()
    record.name = name
    record.description = description
    record.cost = cost
    db.session.commit()
    filtered_menu = MenuItem.query.filter_by(res_id=res_id).all()
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
        record = MenuItem.query.filter_by(_id=modify_id[1]).all()
        return render_template("res_owner/modifymenuitempage.html", record=record)

    else:
        record = MenuItem.query.filter_by(_id=modify_id[1]).all()
    for rec in record:
        db.session.delete(rec)
        db.session.commit()
        db.session.close()
    filtered_menu = MenuItem.query.filter_by(res_id=session['rest_id']).all()
    return render_template("res_owner/editmenupage.html", menu=filtered_menu)


# route for handling the login page logic
@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if not(session.get('logged_in')):
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
                        session["order_cost"] = 0.0
                        session['menu_item_list'] = []
                        session['quantity_list'] = []
                        return render_template("user/user_homepage.html", user=pass_real.name)
                    else:
                        error = 'Invalid Username/Password.'
                elif user_type == "rest_owner":  # Restaurant owner login validation
                    pass_real = RestaurantWhole.query.filter_by(email=email).first()
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
            return render_template("login/login.html", error=error)
    else:
        if session['user_type'] == "customer":
            user_id = int(session['user_id'])
            record = Customer.query.filter_by(_id=user_id).first()
            return render_template("user/user_homepage.html", user=record.name)
        elif session['user_type'] == "rest_owner":
            rest_id = int(session['rest_id'])
            record = RestaurantWhole.query.filter_by(_id=rest_id).first()
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
        record = RestaurantWhole(email, rest_name, owner_name, password, address, zipcode, rating)
        db.session.add(record)
        db.session.commit()
        return render_template("register/register_success.html", error=error)


@app.route("/logout")
def logout_user():
    session.clear()
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

@app.route("/add_billing_address")
def add_billing_address():
    return render_template("address/user_billing_address.html")

@app.route("/process_add_billing_address", methods=['POST'])
def complete_billing_address():
    if session['logged_in'] and session['user_type'] == 'customer':
        apt     = request.form["apt"]
        line1   = request.form["line1"]
        line2   = request.form["line2"]
        city    = request.form["city"]
        state   = request.form["state"]
        zipcode = request.form['zipcode']
        new_address = Address(line1, apt, line2, city, state, zipcode, session['user_id'])
        db.session.add(new_address)
        db.session.commit()
        return render_template("address/address_add_success.html")

@app.route("/addresses")
def existing_addresses():
    if session['logged_in']:
        addresses = Address.query.filter_by(user_id=session['user_id']).all()
        addresses_refined = [str(x).split(",") for x in addresses]
        return render_template("address/existing_addresses.html", addresses=addresses_refined)

@app.route("/delete_address/<id>")
def delete_address(id):
    db.session.delete(Address.query.get(id))
    db.session.commit()
    addresses = Address.query.filter_by(user_id=session['user_id']).all()
    addresses_refined = [str(x).split(",") for x in addresses]
    return render_template("address/existing_addresses.html", addresses=addresses_refined)


def main():
    #ORMTests.run_all()
    #ControllerTests.run_all(app)
    app.debug = True
    app.run(host='127.0.0.1')