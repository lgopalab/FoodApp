from flask import session
from models.customer import CustomerTest as Customer
from models.admin import AdminTest as Admin
from models.restaurant_whole import RestaurantWholeTest as RestaurantWhole

class LoginTests:
	# login as customer
	# login as restaurant owner
	# login as admin

	@staticmethod
	def login_as_customer(app):
		user = Customer.query.first()
		credentials = {"email": user.email,
		               "password": user.password,
		               "login_type": "customer"}
		with app as c:
			req = c.post("/login", data=credentials)
			assert req.status_code == 200
			assert session['logged_in']
			assert session['user_id'] == user._id
			assert session['user_type'] == 'customer'
			assert c.get("/logout").status_code == 200
			assert session.get('logged_in', False) == False
			print "Login test for customer was successful."

			# empty password test
			credentials["password"] = ""
			assert "Both E-mail and Password" in c.post("/login", data=credentials).data
			print "Login test for customer with empty password fail was successful"

			# admin not in db test
			credentials["email"] = "notadmin@foodapp.com"
			credentials["password"] = "notpassword"
			assert 'User Not found' in c.post("/login", data=credentials).data
			print "Login test for non-existing user was successful."

	@staticmethod
	def login_as_admin(app):
		admin = Admin.query.first()
		credentials = {"email": admin.email,
		               "password": admin.password,
		               "login_type": "admin"}
		with app as c:
			req = c.post("/login", data=credentials)
			assert req.status_code == 200
			assert session['logged_in']
			assert session['admin_id'] == admin._id
			c.get("/logout").status_code == 200
			print "Login test for admin was successful."

			# empty password test
			credentials["password"] = "";
			assert "Both E-mail and Password" in c.post("/login", data=credentials).data
			print "Login test for admin with empty password fail was successful"

			# admin not in db test
			credentials["email"] = "notadmin@foodapp.com"
			credentials["password"] = "notpassword"
			assert "Admin not found" in c.post("/login", data=credentials).data
			print "Login test for non existing admin was successful"

	@staticmethod
	def login_as_res_owner(app):
		res_owner = RestaurantWhole.query.first()
		credentials = {"email": res_owner.email,
		               "password": res_owner.password,
		               "login_type": "rest_owner"}
		with app as c:
			req = c.post("/login", data=credentials)
			assert req.status_code == 200
			assert session['logged_in']
			assert session['rest_id'] == res_owner._id
			assert 'Hi!' in req.data
			assert c.get("/logout").status_code == 200
			print "Login test for restaurant owner was successful."

	@staticmethod
	def run_all(app):
		print "Running tests on Login Controller"
		test_client = app.test_client()
		LoginTests.login_as_customer(test_client)
		LoginTests.login_as_res_owner(test_client)
		LoginTests.login_as_admin(test_client)