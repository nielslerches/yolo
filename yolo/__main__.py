import os
import shutil
import sys

sys.dont_write_bytecode = True

shutil.rmtree(os.path.dirname(os.path.abspath(__file__)))
