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

import app.models.admin as a
import load.setup_admin as b

if __name__ == "__main__":
  b.main()
