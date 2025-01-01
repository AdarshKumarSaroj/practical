def checkprime(n):
    if (n>=2):
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return (f"False,{n} is not a prime number")
        return True
    else:
        return "INVALID INPUT"

def genprime(a):
    Prime = []
    for i in range(2,a+1):
        if checkprime(i)==True:
            Prime.append(i)
        else:
            pass
    return(f"List of prime numbers till {a} is : {Prime}")

def genfrstprime(b):
    Prime1 = []
    i = 2
    while(len(Prime1)<b):
        if(checkprime(i)) == True:
            Prime1.append(i)
        i+=1
    if Prime1==[]:
        return(f"NO PRIME NUMBER EXISTS TILL {b}")
    else:
        return(f"LIST OF FIRST {b} PRIME NUMBERS IS:{Prime1}")
num = int(input('Enter a number:'))
if checkprime(num)== True:
    print(num,"is a prime number")
else:
    print(checkprime(num))
print(genprime(num))
print(genfrstprime(num))
