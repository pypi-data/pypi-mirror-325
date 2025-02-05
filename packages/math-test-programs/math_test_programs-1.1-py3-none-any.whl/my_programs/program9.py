def newtons_law_of_cooling():
    print("""

import numpy as np
from sympy import *
from matplotlib import pyplot as plt

t2 = 20
t1 = 100
T=75
t=10

k1 = (1/t)*log((t1-t2)/(T-t2))
print(('k = ',k1))

k = Symbol('k')
t = Symbol('t')
T = Function('T')(t)

T = t2+(t1-t2)*exp(-k*t)
print('T = ' , T)

T = T.subs(k,k1)

T= lambdify(t,T)

t_vals = np.linspace(0,70)

plt.plot(t_vals,T(t_vals),color = 'r')
plt.grid(True)
plt.show()


print('When time t=30 minute T is', T(30), '°C')    
    
    
    
    """)