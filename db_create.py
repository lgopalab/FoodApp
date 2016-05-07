import os
import sys

dir_name1 = os.path.abspath('./app')
dir_name2 = os.path.abspath('./config')
dir_name3 = os.path.abspath('./load')
dir_name4 = os.path.abspath('./data')
sys.path.append(dir_name1)
sys.path.append(dir_name2)
sys.path.append(dir_name3)
sys.path.append(dir_name4)
print sys.path

models = ['address', "admin", "customer", "menu_item",
          "order_details", "order_list", "restaurant_whole"]
setups = ['setup_admin', 'setup_menu_item', 'setup_restaurants_whole', 'setup_users']

for model in models:
	try:
		# exec('from models import %s' % model)
		# exec('%s.main()' % model)
		pass
	except BaseException as e:
		print model
		print e

for model in setups:
	try:
		exec ('from load import %s' % model)
		exec ('%s.main()' % model)
	except BaseException as e:
		print model
		print e
