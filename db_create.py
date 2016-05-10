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

import app.models.customer as cus
import app.models.admin as adm
import app.models.restaurant_whole as res
import app.models.menu_item as men
import app.models.card_details as car
import app.models.address as add
import app.models.order_details as od
import app.models.order_list as ol

import load.setup_admin as sadd
import load.setup_restaurants_whole as sres
import load.setup_users as scus
import load.setup_menu_item as smen

cus.main()
adm.main()
res.main()
men.main()
car.main()
add.main()
od.main()
ol.main()

sadd.main()
sres.main()
scus.main()
smen.main()