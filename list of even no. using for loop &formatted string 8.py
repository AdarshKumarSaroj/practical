#CREATING LIST OF EVEN NUMBERS USING:-(a)For loop
def crt_list_using_for_loop(m):
    lst=[]
    for i in range (0,m+1,2):
        a = i**3
        lst.append(a)
    return lst
### (b):- Using Formatted string
def crt_lst_using_list_comp():
    lst1 =[i**3 for i in range(0,m+1,2)]
    return lst1
m = int(input("Enter number upto cubes to be printed:"))
print(crt_list_using_for_loop(m))
print(crt_lst_using_list_comp())
