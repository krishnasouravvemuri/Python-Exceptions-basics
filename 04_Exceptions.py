import math

val = int(input("Enter value : "))
base = int(input("Enter base : "))

loga = math.log(val , base)

class lessthan1(Exception):
    pass

try :
    if(loga > 1):
        print("logarithmic value is " ,loga)
    else:
        raise lessthan1("Value is less than 1")

except lessthan1 as e :
    print(e)
