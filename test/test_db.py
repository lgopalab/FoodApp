from app.util.database import db
from app.models.restauarant import Restaurant
from app.models.customer import Customer

class Tests:

	@staticmethod
	def test_restaurant_deletion():
		n = len(Restaurant.query.all())
		tulips = Restaurant.query.filter(Restaurant.name == 'Tulips').first()
		db.session.remove(tulips)
		db.session.commit()
		assert (n-1) == len(Restaurant.query.all())

	@staticmethod
	def test_restaurant_insertion():
		n = len(Restaurant.query.all())
		db.session.add(Restaurant("Tulips", "12345 North Tryon", 28232, 4.5))
		db.session.commit()
		assert (n+1) == len(Restaurant.query.all())

	@staticmethod
	def test_customer_deletion():
		n = len(Customer.query.all())
		db.session.add(Customer("bob@bob.com", "bob", "bobpwd", "address_of_bob", 11111))
		db.session.commit()
		assert (n+1) == len(Customer.query.all())


	@staticmethod
	def test_customer_insertion():
		n = len(Customer.query.all())
		bob = Customer.query.filter(Customer.name == 'bob').first()
		db.session.remove(bob)
		db.session.commit()
		assert (n - 1) == len(Customer.query.all())

	@staticmethod
	def run_all():
		Tests.test_customer_insertion()
		Tests.test_customer_deletion()

		Tests.test_restaurant_insertion()
		Tests.test_restaurant_deletion()

