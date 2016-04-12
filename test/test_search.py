from app.models.restaurant import Restaurant

class Tests:
	@staticmethod
	def test_search_positive():
		assert len(Restaurant.query.filter(Restaurant.name.startswith('Bo')).all()) == 1

	@staticmethod
	def test_search_negative():
		assert Restaurant.query.filter(Restaurant.name.startswith('xyz')).all() == []


	@staticmethod
	def run_all():
		Tests.test_search_positive()
		Tests.test_search_negative()


