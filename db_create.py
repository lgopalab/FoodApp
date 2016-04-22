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

from app.models import admin, customer, menu_item, order_list, restaurant_whole, order_details
from load import setup_admin, setup_users, setup_menu_item, setup_restaurants_whole