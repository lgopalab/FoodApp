from app.models.menu_item import Menu_item
from app.util.database import db

if __name__ == "load.setup_menu_item":
	with open('data/sample_menu_item.txt') as f:
		db.session.query(Menu_item).delete()
		db.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			db.session.add(Menu_item(int(record[0]), record[1], record[2], float(record[3]),int(record[4])))
		db.session.commit()
