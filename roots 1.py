#####PROGRAM-1: TO FIND ROOTS OF A QUADRATIC EQUATION  #######ax**2 + b*x + c
import math
def findroots(a,b,c):
    d= b**2-4*a*c
    if d>=0:
        print('real roots exist')
        print('X1 =', (-b+math.sqrt(d))/(2*a))
        print('X2 =', (-b-math.sqrt(d))/(2*a))
    else:
        print("Real roots do not exist")
m= int(input('enter value of a:'))
n= int(input('enter value of b:'))
p= int(input('enter value of c:'))
findroots(m,n,p)
