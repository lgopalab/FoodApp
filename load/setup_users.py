from app.models.customer import Customer
from app.util.database import db
from app.models.customer import CustomerTest
from app.util.database import db2

# | _id | email             | name     | password | address | zipcode |
# |   4 | dpanchan@uncc.edu | Dinesh   | 123      |         |       0 |

def main():
	with open('data/sample_users.txt') as f:
		db.session.query(Customer).delete()
		db.session.commit()
		db2.session.query(CustomerTest).delete()
		db2.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			db.session.add(Customer(record[1], record[2], record[3], record[4], int(record[5])))
			db2.session.add(CustomerTest(record[1], record[2], record[3], record[4], int(record[5])))
		db.session.commit()
		db2.session.commit()