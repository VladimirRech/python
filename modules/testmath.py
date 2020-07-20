# testmath.py
# Testing many features of python

import mymath
import sys              # System library

# It's possible get the name of procces and to know if I'm in a script on 
# interpreter. We can run any python file stand alone

if __name__ == "__main__" and len(sys.argv) > 0:
    print("On main module");
    
    if len(sys.argv) > 1:
        print(mymath.fib(int(sys.argv[1])))