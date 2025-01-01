def find_substring_indices(main_string, substring):
    indices = []
    for i in range(len(main_string) - len(substring) + 1):
        if main_string[i:i+len(substring)] == substring:
            indices.append(i)
    if indices == []:
        return -1
    else:
        return indices

str1 = input("ENTER A STRING: ")
str2 = input("ENTER ANOTHER STRING: ")
print(find_substring_indices(str1, str2))

