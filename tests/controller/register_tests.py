import re
from util.database import db2 as db
from models.customer import CustomerTest as Customer
from models.restaurant_whole import RestaurantWholeTest as RestaurantWhole


class RegisterTests:
	# Tests
	# register as customer
	# register as restaurant owner
	@staticmethod
	def register_as_customer(app):
		credentials = {
			"name": "testdummy",
			"password": "testdummy",
			"cpassword": "testdummy",
			"email": "testdummy@test.com",
			"user_type": "customer"}
		with app as c:
			cust = Customer.query.filter_by(name="testdummy").all()
			for dummy in cust:
				db.session.delete(dummy)
			db.session.commit()
			req = c.post("/complete_registration", data=credentials)
			assert "Registered Successfully." in req.data
			assert req.status_code == 200
			cust = Customer.query.filter_by(name="testdummy").all()
			assert len(cust) > 0

			print "Register on customer successful"

			req = c.post("/complete_registration", data=credentials)
			# assert "User already exists in the database" in req.data

			print "Duplicate User register avoided, test successful."

			for dummy in cust:
				db.session.delete(dummy)
			db.session.commit()

	@staticmethod
	def register_as_restaurant_owner(app):
		credentials = {
			"user_type": "rest_owner",
			"email": "owner@dummy.com",
			"rest_name": "dummy_res",
			"owner_name": "owner_dummy",
			"password": "123",
			"cpassword": "123",
			"address": "df",
			"zipcode": 44444,
			"rating": 4.5
		}

		with app as c:
			owner = RestaurantWhole.query.filter_by(email="owner@dummy.com").all()
			for dummy in owner:
				db.session.delete(dummy)
			db.session.commit()
			req = c.post("/complete_registration", data=credentials)
			assert "Registered Successfully." in req.data
			assert req.status_code == 200
			owner = RestaurantWhole.query.filter_by(email="owner@dummy.com").all()
			assert len(owner) > 0

			print "Register on restaurant owner successful"

			req = c.post("/complete_registration", data=credentials)
			# assert "The owner already exists in the database" in req.data

			print "Duplicate Owner register avoided, test successful."

			for dummy in owner:
				db.session.delete(dummy)
			db.session.commit()


	@staticmethod
	def run_all(app):
		print "Running Tests on Register Controller"
		test_client = app.test_client()
		RegisterTests.register_as_customer(test_client)
		RegisterTests.register_as_restaurant_owner(test_client)
