from models.menu_item import Menu_item
from models.restaurant_whole import Restaurant_whole
from util.database import db

'''menu_items
	add / modify / delete / search'''
# res_id, name, description, cost, rating
class Tests:

	@staticmethod
	def test_menu_item_insertion(res_id, menu):
		print "running tests on menu items insertion"
		n = len(Menu_item.query.filter(Menu_item.res_id == res_id).all())
		m = len(menu)
		for item in menu:
			db.session.add(Menu_item(item[0], item[1], item[2], item[3], item[4]))
		db.session.commit()
		assert len(Menu_item.query.all()) == n + m


	@staticmethod
	def test_menu_item_modification(res, menu):
		print "running tests on menu items modification"
		items = []
		for i, item in enumerate(Menu_item.query.filter(Menu_item.res_id == res).all()):
			item.description = menu[i][2]
			items.append([item.description, i])
		db.session.commit()




	@staticmethod
	def test_menu_item_deletion(res):
		print "running tests on menu items deletion"
		for item in Menu_item.query.filter(Menu_item.res_id == res).all():
			db.session.delete(item)
		db.session.commit()
		assert 0 == len(Menu_item.query.all())


	@staticmethod
	def match_menu_of_a_restaurant(res_id, menu):
		menu_fetched = Menu_item.query.filter(Menu_item.res_id == res_id).all()
		for (a, b) in zip(menu, menu_fetched):
			assert a[1] == b.name
			assert a[2] == b.description
			assert a[3] == b.cost
			assert a[4] == b.rating


	@staticmethod
	def run_all():
		""" we know this restaurant exists"""
		# |   1 | joe@arby.com                | Arby's
		Tests.test_menu_item_deletion(1)
		Tests.match_menu_of_a_restaurant(1, [])
		menu = [[1, "Burger", "Burger description", 10.3, 4],
		        [1, "Sandwich", "Sandwich description", 12.5, 3],
		        [1, "Pizza", "Pizza description", 13, 5]]
		Tests.test_menu_item_insertion(1, menu)
		Tests.match_menu_of_a_restaurant(1, menu)
		menu[0][2] = "changed burger desc"
		menu[1][2] = "changed sandwich desc"
		menu[2][2] = "changed burger desc"
		Tests.test_menu_item_modification(1, menu)
		Tests.match_menu_of_a_restaurant(1, menu)
		Tests.test_menu_item_deletion(1)
		if Menu_item.query.all() == []:
			Tests.test_menu_item_insertion(1, menu)


