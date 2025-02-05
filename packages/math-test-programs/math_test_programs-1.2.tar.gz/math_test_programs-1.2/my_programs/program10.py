def consistency_solution():
    print("""
    
#This is program of consistency of solutions [prog - 10]

import numpy as np

a = np.matrix([[1,2,-1],[2,1,4],[3,3,4]])
b = np.matrix([[1],[2],[1]])
AB = np.concatenate((a,b),axis = 1)
ra = np.linalg.matrix_rank(a)
rab = np.linalg.matrix_rank(AB)
n = a.shape[1]

if(ra==rab):
    if(ra==n):
        print("The sytsem has unique solution")
        print(np.linalg.solve(a,b))
    else:
        print("The system has infinitely many solutions")
else:
    print("The system of equations is inconsistent")

    
    
    
    """)