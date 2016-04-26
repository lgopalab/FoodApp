from models.customer import Customer
from models.address import Address
from util.database import db

class AddressTests:

	@staticmethod
	def add_address_test(app):
		user = Customer.query.first()
		with app as c:
			credentials = {
				"login_type": "customer",
				"email": user.email,
				"password": user.password
			}
			address = {
				"line1": "line1",
				"apt": "D",
				"line2": "line2",
				"city": "charlotte",
				"state": "NC",
				"zipcode": 28262
			}

			res = c.post("/login", data=credentials)
			assert 'Hi' in res.data

			res2 =  c.post("process_add_billing_address", data=address)
			assert "The Address was saved successfully" in res2.data

			dummy_address = Address.query.filter_by(line1="line1", line2="line2").all()
			for address in dummy_address:
				if address.user_id == user._id:
					db.session.delete(address)
			db.session.commit()

			print "Add address test successful"


	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		AddressTests.add_address_test(test_client)