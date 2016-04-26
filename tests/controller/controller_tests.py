from flask import session
from login_tests import LoginTests
from register_tests import RegisterTests
from static_page_tests import PageRetrievalTests
from search_tests import SearchTests



class ControllerTests:
	@staticmethod
	def run_all(app):
		print "::Controller Test Suite::"
		PageRetrievalTests.run_all(app)
		RegisterTests.run_all(app)
		LoginTests.run_all(app)
		SearchTests.run_all(app)
