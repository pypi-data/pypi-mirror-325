def first_order_diff_eqn():
    print("""


#This is program from solution of first order equation [prog - 8]
from sympy import *

x , y = symbols('x , y')

y = Function("y")(x)

y1 = Derivative(y,x)
z1 = dsolve(Eq(x**3*y1-x**2*y+y**4*cos(x),0),y)
print(z1)
    
    
    
    """)