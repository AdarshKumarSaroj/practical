###PROGRAM12 :-(a) Split a tuple in half
t1 = (1,2,5,7,9,2,4,6,8,10)
l1= list(t1)
a = int(len(l1)/2)
print(l1[0:a])
print(l1[a:])


###PROGRAM12 :-(b)
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
t2 = tuple(l2)
print(t2)
####PROGRAM12 :-(c)
t3 = (11,13,15)
l3 = list(t3)
l13 = l1 + l3
t13 = tuple(l13)
print(t13)

maxi = max(l13)
print("maximum value of this tuple is",maxi)
mini = min(l13)
print("minimum value of this tuple is",mini)
