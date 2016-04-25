import customer_tests
import menu_item_tests
import res_whole_tests


class ORMTests:
	@staticmethod
	def run_all():
		print ":::TESTS:::"
		customer_tests.Tests.run_all()
		menu_item_tests.Tests.run_all()
		res_whole_tests.Tests.run_all()
