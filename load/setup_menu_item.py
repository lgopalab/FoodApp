from app.models.menu_item import Menu_item
from app.util.database import db

db.create_all()

with open('../data/sample_menu_item.txt') as f:
	data = f.readlines()
	records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
	for record in records:
		db.session.add(Menu_item(int(record[0]), record[1], record[2], float(record[3]),int(record[4])))
	db.session.commit()
	