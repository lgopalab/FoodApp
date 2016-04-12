from app.models.restaurant_whole import Restaurant_whole
from app.util.database import db

db.create_all()

def main():
    with open('data/sample_restaurants_whole.txt') as f:
        data = f.readlines()
        records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
        for record in records:
            db.session.add(Restaurant_whole(record[0], record[1], record[2], record[3],record[4], int(record[5]), int(record[6])))
        db.session.commit()
