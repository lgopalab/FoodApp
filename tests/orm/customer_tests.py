from models.customer import CustomerTest as Customer
from util.database import db2 as db

class Tests:
	@staticmethod
	def test_customer_insertion():
		print "running tests on customer insertion"
		n = len(Customer.query.all())
		db.session.add(Customer("bob@bob.com", "bob", "bobpwd", "address_of_bob#", 11111))
		db.session.commit()
		assert (n + 1) == len(Customer.query.all())


	@staticmethod
	def test_customer_deletion():
		print "running tests on customer deletion"
		n = len(Customer.query.all())
		bob = Customer.query.filter(Customer.name == 'bob').first()
		db.session.delete(bob)
		db.session.commit()
		assert (n - 1) == len(Customer.query.all())

	@staticmethod
	def test_customer_authentication():
		print "running tests on customer authentication"
		"we know bob:bobpwd exists in the system"
		bob = Customer.query.filter(Customer.name == 'bob').first()
		assert bob.password == 'bobpwd'

	@staticmethod
	def test_customer_validation():
		print "running tests on customer validation"
		bob = Customer("bob@bob.com", "bob", 'bobpwd', 'address_of_bob$', 11111)
		db.session.add(bob)
		db.session.commit()
		bob = Customer.query.filter(Customer.name=='bob').first()
		try:
			assert bob != None
			assert bob.email == 'bob@bob.com'
			assert bob.name == 'bob'
			assert bob.password == 'bobpwd'
			assert bob.address == 'address_of_bob$'
			assert bob.zipcode == 11111
			Tests.test_customer_authentication()
		except AssertionError as e:
			raise AssertionError(e)
		finally:
			db.session.delete(bob)
			db.session.commit()

	@staticmethod
	def test_customer_modification():
		pass

	@staticmethod
	def run_all():
		Tests.test_customer_insertion()
		Tests.test_customer_deletion()
		Tests.test_customer_validation()
		Tests.test_customer_modification()