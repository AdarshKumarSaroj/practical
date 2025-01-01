class character:
    def __init__(self,char):
        self.char = char
    def checktext(self):
        if self.char.isalpha()== True:
            print("VALID TEXT ------>CONTAINS ONLY ALPHABETS")
        elif self.char.isalnum() == True:
            print("INVALID TEXT----> CONTAINS NUMERIC CHARACTERS")
        else:
            print("INVALID TEXT----> CONTAINS SPECIAL CHARACTERS")
try:
    char = input("ENTER TEXT:")
    CHECKER = character(char)
    CHECKER.checktext()
except Exception as e:
    print(f"InvalidNameError:{e}")
