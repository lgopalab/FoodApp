class SearchTests:
	@staticmethod
	def one_restaurant(app):
		print "Running tests on Search Controller"
		assert 'Arby' in app.get("/search_restaurants?resname=A").data
		assert "Bojangles" in app.get("/search_restaurants?resname=Bo").data
		print "Search test was successful."


	@staticmethod
	def run_all(app):
		test_client = app.test_client()
		SearchTests.one_restaurant(test_client)