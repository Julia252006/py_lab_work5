import sys
sys.path.append("C/scripts")
sys.path.append("./Defs")
import py_lab_5.work_2.definitions as defs
from main import *

main_var = "main.py"

if __name__ == "__main__":
    defs.functionTwo(main_var)
else:
    print("Execution module:{}".format(__file__))