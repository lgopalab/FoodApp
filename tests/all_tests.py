import customer_tests
import restaurant_tests
import res_whole_tests
import menu_item_tests

class Tests:
	@staticmethod
	def run_all():
		print ":::TESTS:::"
		customer_tests.Tests.run_all()
		restaurant_tests.Tests.run_all()
		menu_item_tests.Tests.run_all()
		res_whole_tests.Tests.run_all()
