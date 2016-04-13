from util.database import db
from models.restaurant import Restaurant

class Tests:
	@staticmethod
	def test_restaurant_insertion():
		print "running tests on restaurant insertion"
		n = len(Restaurant.query.all())
		db.session.add(Restaurant("Tulips", "12345 North Tryon", 28232, 4.5))
		db.session.commit()
		assert (n + 1) == len(Restaurant.query.all())

	@staticmethod
	def test_restaurant_deletion():
		print "running tests on restaurant deletion"
		n = len(Restaurant.query.all())
		tulips = Restaurant.query.filter(Restaurant.name == 'Tulips').first()
		db.session.delete(tulips)
		db.session.commit()
		assert (n-1) == len(Restaurant.query.all())

	@staticmethod
	def test_search_positive():
		print "running tests on restaurant search - positive test"
		assert len(Restaurant.query.filter(Restaurant.name.startswith('Arby')).all()) == 1

	@staticmethod
	def test_search_negative():
		print "running tests on restaurant search - negative test"
		assert Restaurant.query.filter(Restaurant.name.startswith('xyz')).all() == []

	@staticmethod
	def run_all():
		Tests.test_restaurant_insertion()
		Tests.test_restaurant_deletion()

		Tests.test_search_negative()
		Tests.test_search_positive()

