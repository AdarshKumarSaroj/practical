class Copyfile:
    def __init__(self,file,file1,file2):
        self.file = file
        self.file1 = file1
        self.file2 = file2

    def copy(self):
        try:
            file = open(self.file,'r')
            file1 = open(self.file1,'w')
            file2 = open(self.file2,'w')
            content1 = file.readlines()
            for a in content1:
                if ((content1.index(a))%2)==0:
                    file2.write(a)
                else:
                    file1.write(a)
            file.close()
            file1.close()
            file2.close()
            print("File Copied Successfully")
        except Exception as e:
            print("An Error Occured:",e)

copydone = Copyfile("index.txt","file1.txt","file2.txt")
# Jaa ke index.txt file banao phele uske vejse se a rha hai error
copydone.copy()
