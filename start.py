import os
import sys

dir_name = os.path.abspath('./app')
sys.path.append(dir_name)
print sys.path

import app.controllers.app as a

if __name__ == "__main__":
  a.main()
