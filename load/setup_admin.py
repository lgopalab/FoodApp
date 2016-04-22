from app.models.admin import Admin
from app.util.database import db

# | _id | email             | name     | password | address | zipcode |
# |   4 | dpanchan@uncc.edu | Dinesh   | 123      |         |       0 |

if __name__ == "load.setup_admin":
	with open('data/sample_admin.txt') as f:
		db.session.query(Admin).delete()
		db.session.commit()
		data = f.readlines()
		records = [[_.strip() for _ in res.strip().strip('|').split('|')] for res in data]
		for record in records:
			print record[0]
			db.session.add(Admin(record[0], record[0]))
			db.session.commit()
