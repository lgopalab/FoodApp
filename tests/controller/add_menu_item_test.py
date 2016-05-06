from models.restaurant_whole import Restaurant_whole
from models.menu_item import Menu_item
from util.database import db

class AddMenuTests:

	@staticmethod
	def add_menu_item_test(app):
		res = Restaurant_whole.query.first()
		with app as c:
			credentials = {
				"login_type": "rest_owner",
				"email": res.email,
				"password": res.password
			}
			address = {
				"line1": "line1",
				"apt": "D",
				"line2": "line2",
				"city": "charlotte",
				"state": "NC",
				"zipcode": 28262
			}

			resp = c.post("/login", data=credentials)

			item = {
				"inputName": "Icecream Sandwich",
				"cost": 10,
				"description": "icecream inside sandwich"
			}

			c.post("/addmenuitem", data=item)
			assert len(Menu_item.query.filter_by(res_id=res._id,
			                                     cost=item['cost'],
			                                     description = item['description'],
			                                     name=item["inputName"]).all()) == 1

			for item in Menu_item.query.filter_by(res_id=res._id, name=item["inputName"]).all():
				db.session.delete(item)
			db.session.commit()

			c.get("/logout")
			print "Add menu item test successful"


	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		AddMenuTests.add_menu_item_test(test_client)