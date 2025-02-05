def ang_btwn_two_curves():
    print("""
     #This is the Program for Angle between two curves [Prog number 3]

    
from sympy import *

r,t = symbols('r , t')

r1 = 4*(1+cos(t))
r2 = 5*(1-cos(t))

dr1 = diff(r1,t)
dr2 = diff(r2,t)

t1 = r1/dr1
t2 = r2/dr2

q = solve(r1-r2,t) #q is a list of all possible values of t, where t is when r1-r2 become zero

w1 = t1.subs({t:float(q[1])})
w2 = t2.subs({t:float(q[1])})

y1 = atan(w1)
y2 = atan(w2)

w = abs(y1-y2)

print(f"Angle between the curves is {w}")
    
    
    
    
    
    """)
