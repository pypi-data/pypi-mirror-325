def linear_congurence():
    print("""
    
#This is program for Linear Congurence(Program-13)
from sympy import *
# Linear congruence
# Consider ax=b(mod m),x is called the solution of the congrunce
a=int( input ('enter integer a ') ) ; #7
b=int( input ('enter integer b ') ) ; #9
m=int( input ('enter integer m ') ) ; #15
d=gcd (a , m )
if ( b%d!=0 ):
    print ('the congruence has no integer solution ') ;
else :
    for i in range (1 , m-1 ):
        x=( m/a )*i+( b/a )

        if( x // 1==x ):# check whether x is an integer
            print ('the solution of the congruence is ', x )
            break
""")




