# Example content for program1.py
def sin_cos_wave():
    print("""
    #This is the Program for Sine-Cos Wave [Prog number 1]

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-10,10,0.001)

y1 = np.sin(a)
y2 = np.cos(a)

plt.plot(a,y1,a,y2)

plt.title("sine and Cosine Wave")
plt.xlabel("Value of x")
plt.ylabel("Values of sin(x) and cos(x)")

plt.grid(True)

plt.show()


""")
