a = int(input("Enter a number : "))

class Notdivby2(Exception): #defining a custom exception
    pass

try :
    if(a%2 == 0):
        print("all good")
    else:
        raise Notdivby2("Number is odd") #giving a condition for the exception
except Notdivby2 as e: # catching the exception
    print(f"error caught , that is '{e}' ")