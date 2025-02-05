#This is the Program for Angle of curve at pi/2 [Prog number 4]
def ang_curve_at_pi_2():
    print("""

from sympy import *

r , t = symbols('r  t')

r1 = 4 * (1+cos (t))

dr1 = diff(r1 , t)

dr2 = diff(dr1 , t)

rho = (r1**2 + dr1**2) ** (1.5)/ (r1**2 + 2*dr1**2 - r*dr2)

rho1 = rho.subs(t , pi/2)

print(f"The radius of curvature is {rho1}")   
    
    
    
    """)

