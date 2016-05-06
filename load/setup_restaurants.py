from app.models.restaurant import Restaurant
from app.util.database import db

if __name__ == "load.setup_restaurants":
	with open('../data/sample_restaurants.txt') as f:
		db.session.query(Restaurant).delete()
		db.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			db.session.add(Restaurant(record[0], record[1], int(record[2]), int(record[3])))
		db.session.commit()
