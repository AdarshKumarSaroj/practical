
####PROGRAM-3 : TO GENERATE A PYRAMID AND A REVERSE PYRAMID.#####
n = int(input("Enter number of rows: "))
def pyramid(n):
    for i in range(0,n):    
        print(' '*(n-i-1), '*'*(2*i+1))



def reverse_pyrimad(n):
    for i in range(1,n+1):    
        print(' '*(2*n-2+i), '*'*(2*(n-i)+1))

pyramid(n)
reverse_pyrimad(n)