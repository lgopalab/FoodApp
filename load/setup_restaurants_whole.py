from app.models.restaurant_whole import RestaurantWhole
from app.util.database import db

from app.models.restaurant_whole import RestaurantWholeTest
from app.util.database import db2

def main():
    with open('data/sample_restaurants_whole.txt') as f:
        db.session.query(RestaurantWhole).delete()
        db.session.commit()
        db2.session.query(RestaurantWholeTest).delete()
        db2.session.commit()
        data = f.readlines()
        records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
        for record in records:
            db.session.add(RestaurantWhole(record[0], record[1], record[2], record[3], record[4], int(record[5]), int(record[6])))
            db2.session.add(
	            RestaurantWholeTest(record[0], record[1], record[2], record[3], record[4], int(record[5]), int(record[6])))

        db.session.commit()
        db2.session.commit()

