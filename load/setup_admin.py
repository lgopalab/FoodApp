from app.models.admin import Admin
from app.models.admin import AdminTest

from app.util.database import db2
from app.util.database import db

# | _id | email             | name     | password | address | zipcode |
# |   4 | dpanchan@uncc.edu | Dinesh   | 123      |         |       0 |

def main():
	with open('data/sample_admin.txt') as f:
		db.session.query(Admin).delete()
		db2.session.query(AdminTest).delete()
		db.session.commit()
		db2.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			db.session.add(Admin(record[0], record[0]))
			db2.session.add(AdminTest(record[0], record[0]))
		db.session.commit()
		db2.session.commit()

