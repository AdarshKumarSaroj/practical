def findfreq(char,a):
    count=0
    for i in char:
        if i==a:
            count+=1
        else:
            pass
    return count

def repchar(char,a,b):
    char_lst = list(char)
    for i in range(len(char_lst)):
        if char_lst[i]== a:
            char_lst[i]= b
        new_str = "".join(char_lst)
    return new_str
    
def rmvchar(char,a):
    char_lst = list(char)
    for i in range(len(char)):
        if char_lst[i] == a:
            del (char_lst[i])
            break
        new_str = "".join(char_lst)
    return new_str

def rmvall(char,a):
    char_lst = list(char)
    n_lst = [i for i in char if i!=a]
    new_str = "".join(n_lst)
    return new_str

char = input("ENTER A STRING:")
chr1 = input("ENTER CHARACTER 1 :")
chr2 = input("ENTER CHARACTER 2 :")
print(findfreq(char,chr1))
print(repchar(char,chr1,chr2))
print(rmvchar(char,chr1))
print(rmvall(char,chr1))
