from pprint import pprint
import jinja2
import re

class PageRetrievalTests:
	@staticmethod
	def run_all(app):
		pages = ["/", "/home", "/login", "register", "search"]
		for page in pages:
			assert app.test_client().get(page).status_code == 200

class RegisterTests:
	# Tests
	# register as customer
	# register as restaurant owner
	@staticmethod
	def register_as_customer(app):
		post_req = app.post("/register_form", data = {'user_type': 'customer'})
		assert post_req.status_code == 200
		html = post_req.data
		# print html
		html = re.search('<h1>.*</h1>', html)
		# print '*' * 80, html

	@staticmethod
	def register_as_restaurant_owner(app):
		pass

	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		RegisterTests.register_as_customer(test_client)
		RegisterTests.register_as_restaurant_owner(test_client)


class LoginTests:
	@staticmethod
	def root_url_page(app):
		assert app.get("/login").status_code == 200

	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		LoginTests.root_url_page(test_client)

class SearchTests:
	@staticmethod
	def one_restaurant(app):
		print "Running tests on Search Controller"
		assert 'Arby' in app.get("/search_restaurants?resname=A").data
		assert "Bojangles" in app.get("/search_restaurants?resname=Bo").data

	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		SearchTests.one_restaurant(test_client)

class ControllerTests:
	@staticmethod
	def run_all(app):
		PageRetrievalTests.run_all(app)
		RegisterTests.run_all(app)
		LoginTests.run_all(app)
		SearchTests.run_all(app)
