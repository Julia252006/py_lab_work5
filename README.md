Brain Academy. Python Course. 

Laboratory Work #5.2
1. Create two modules were import from each other present

```python 
# main.py
import py_lab_5.work_2.definitions as defs

main_var = "main.py"

if __name__ == "__main__":
    defs.functionTwo(main_var)
else:
    print("Execution module:{}".format(__file__))
    
#  difinitions.py
from py_lab_5.work_2.main import *
pi = 3.14

def functionOne():
    print("function one call!")

def functionTwo(arg):
    print("function two call with arg:{}".format(arg))   
```

Laboratory Work #5.3
1. Create two modules were import from each other present
that placed in different folders

```python 
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
```
