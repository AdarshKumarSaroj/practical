class frequency:
    def __init__(self,file_name):
        self.file_name = file_name
        self.D =  {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0, 'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0 ,'w':0,'x':0,'y':0,'z':0}
    def calculate(self):
        try:
            with open (self.file_name,'r') as file:
                content = file.read()
                for char in content:
                    if char in self.D:
                        self.D[char] += 1 
                    else:
                        self.D[char] = 1
            return self.D
        except FileNotFoundError:
            print('THE FILE DOES NOT EXIST')

file_name = input('ENTER NAME OF THE FILE:')
calculator = frequency(file_name)
result= calculator.calculate()
print(result)
