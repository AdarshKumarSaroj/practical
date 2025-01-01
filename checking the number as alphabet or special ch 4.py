def checkchar(char):
    if char.isalpha()== True:
        return "Alphabet"
    elif char.isdigit()== True:
        return "Number"
    else:
        return "Special Character"

def checkcase(char):
    if char.isalpha()== True:
        if char.islower()== True:
            return(f"{char} is lowercase")
        else:
            return(f"{char} is uppercase")
    else:
        pass

def checkdig(char):
    numdict = {1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",0:"ZERO"}
    num_in_wrds= numdict.get(int(char))
    return num_in_wrds

CHAR = input("Enter Something:")
print(checkchar(CHAR))
if checkchar(CHAR)== "Alphabet":
    print(checkcase(CHAR))
elif checkchar(CHAR)== "Number":
    print(checkdig(CHAR))
else:
    print(f"{CHAR} is a Special Character.")
