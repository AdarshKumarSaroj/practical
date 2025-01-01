class Reverse:
    def __init__(self,file1):
        self.file1 = file1

    def reverser(self):
        file1 = open(self.file1,'r')
        content = file1.read()
        content1 = content[::-1]
        return content1

file = input("ENTER FILE NAME:")
reversed = Reverse(file)
print(reversed.reverser())
