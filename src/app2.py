from restaurant_model import db
from restaurant_model import Restaurant
# db.create_all()

'''
with open('sample_data.txt') as f:
	data = f.readlines()
	records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
	for record in records:
		db.session.add(Restaurant(record[0], record[1], int(record[2]), int(record[3])))
	db.session.commit()
'''

print Restaurant.query.filter(Restaurant.name.startswith('Arby')).all()
