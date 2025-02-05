def four_leaved_rose():
    print("""
    #This is the Program for Four-Leaved-Rose [Prog number 2[part-1]]

from pylab import *

theta = linspace(0,2*pi,1000)
r = 2*abs(cos(2*theta))
polar(theta,r,'r')
show()
    """)

def lemniscate():
    print("""
    #This is the Program for Lemniscate[Prog number 2[part-2]]
x,y = symbols('x y')
p5 = plot_implicit(
    Eq(4*(y**2),(x**2)*(4-x**2)),(x,-5,5),(y,-5,5)
)

    """)
