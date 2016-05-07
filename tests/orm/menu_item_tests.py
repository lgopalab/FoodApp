from models.menu_item import MenuItemTest as MenuItem
from util.database import db2 as db

'''menu_items
    add / modify / delete / search'''
# res_id, name, description, cost, rating
class Tests:

    @staticmethod
    def test_menu_item_insertion(res_id, menu):
        print "running tests on menu items insertion"
        n = len(MenuItem.query.filter(MenuItem.res_id == res_id).all())
        m = len(menu)
        for item in menu:
            db.session.add(MenuItem(item[0], item[1], item[2], item[3], item[4]))
        db.session.commit()
        assert len(MenuItem.query.all()) == n + m


    @staticmethod
    def test_menu_item_modification(res, menu):
        print "running tests on menu items modification"
        items = []
        for i, item in enumerate(MenuItem.query.filter(MenuItem.res_id == res).all()):
            item.description = menu[i][2]
            items.append([item.description, i])
        db.session.commit()




    @staticmethod
    def test_menu_item_deletion(res):
        print "running tests on menu items deletion"
        db.session.query(MenuItem).delete()
        db.session.commit()
        assert 0 == len(MenuItem.query.all())


    @staticmethod
    def match_menu_of_a_restaurant(res_id, menu):
        menu_fetched = MenuItem.query.filter(MenuItem.res_id == res_id).all()
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
        if MenuItem.query.all() == []:
            Tests.test_menu_item_insertion(1, menu)


