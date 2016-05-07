from app.models.menu_item import MenuItem
from app.util.database import db
from app.models.menu_item import MenuItemTest
from app.util.database import db2

def main():
	with open('data/sample_menu_item.txt') as f:
		db.session.query(MenuItem).delete()
		db.session.commit()
		db2.session.query(MenuItemTest).delete()
		db2.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			db.session.add(MenuItem(int(record[0]), record[1], record[2], float(record[3]), int(record[4])))
			db2.session.add(MenuItemTest(int(record[0]), record[1], record[2], float(record[3]), int(record[4])))
		db.session.commit()
		db2.session.commit();

