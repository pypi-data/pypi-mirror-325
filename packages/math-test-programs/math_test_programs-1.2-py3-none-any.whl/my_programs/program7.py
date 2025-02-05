def limits():
    print("""

#This is the Program for Limits [Prog number 7 ]

from sympy import *
from math import *

x = Symbol('x')
l = Limit((1+1/x)**x,x,inf).doit()
print(l)
    
    
    
    
    """)