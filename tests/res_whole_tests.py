"""res whole should be open to
	insertion
	deletion
	modification
	search"""

from util.database import db
from models.restaurant_whole import Restaurant_whole
# email, rest_name, owner_name, password, address, zipcode, rating


class Tests:
	@staticmethod
	def test_restaurant_insertion():
		print "running tests on restaurant + owner table insertion"
		n = len(Restaurant_whole.query.all())
		db.session.add(Restaurant_whole("tulipsrestaurant@hotels.com", "Tulips", "Kumar", 'kumar', "12345 North Tryon", 28232, 4.5))
		db.session.commit()
		assert (n + 1) == len(Restaurant_whole.query.all())


	@staticmethod
	def test_restaurant_validation():
		print "running tests on restaurant + owner table validation"
		""" checks if the values are inserted correctly"""
		tulips = Restaurant_whole.query.filter(Restaurant_whole.rest_name == 'Tulips').first()
		assert tulips.rest_name == 'Tulips'
		assert tulips.owner_name == 'Kumar'
		assert tulips.address == "12345 North Tryon"
		assert tulips.rating == 4.5
		assert tulips.zipcode == 29232


	@staticmethod
	def test_restaurant_deletion():
		print "running tests on restaurant + owner table deletion"
		n = len(Restaurant_whole.query.all())
		all_tulips = Restaurant_whole.query.filter(Restaurant_whole.rest_name == 'Tulips').all()
		for tulips in all_tulips:
			db.session.delete(tulips)
		db.session.commit()
		assert (n-1) == len(Restaurant_whole.query.all())

	@staticmethod
	def test_search_positive():
		print "running tests for restaurant + owner table search - positive test"
		assert len(Restaurant_whole.query.filter(Restaurant_whole.rest_name.startswith('Arby')).all()) == 1

	@staticmethod
	def test_search_negative():
		print "running tests for restaurant + owner table search - negative test"
		assert Restaurant_whole.query.filter(Restaurant_whole.rest_name.startswith('xyz')).all() == []

	@staticmethod
	def run_all():
		Tests.test_restaurant_insertion()
		Tests.test_restaurant_deletion()

		Tests.test_search_negative()
		Tests.test_search_positive()
