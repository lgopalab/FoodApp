import os
import sys

dir_name1 = os.path.abspath('./app')
dir_name2 = os.path.abspath('./config')
dir_name3 = os.path.abspath('./load')
dir_name4 = os.path.abspath('./data')
sys.path += [dir_name1,dir_name2,dir_name3,dir_name4]
print sys.path

import app.controllers.app as a

if __name__ == "__main__":
  a.main()