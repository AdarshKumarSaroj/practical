def swapchar(str1,str2,n): 
    swapped_str1 = str2[:n] + str1[n:]
    swapped_str2 =  str1[:n] + str2[n:]
    return swapped_str1 , swapped_str2

str1 = input("ENTER STRING 1:")
str2 = input("ENTER STRING 2:")
NUM = int(input("ENTER NUMBER OF CHARACTERS TO SWAP:"))
print(swapchar(str1,str2,NUM))
