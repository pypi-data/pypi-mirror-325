def mixed_partial_derivative():
    print("""
    
#This is the Program for Mixed partial dervivatives u = exp(x)(xcos(y)-ysin(y)) [Prog number 5]
from sympy import *

x,y = symbols('x  y')
u = exp(x)*(x*cos(y)-y*sin(y))
dux = diff(u , x)
duy = diff(u,y)
duxy = diff(dux , y)
duyx = diff(duy , x)

if duxy == duyx:
    print("mixed Partial derviatives are equal")
else:
    print("Mixed partial derviatives are not equal")
    
    
    
    
    
    
    
    """)