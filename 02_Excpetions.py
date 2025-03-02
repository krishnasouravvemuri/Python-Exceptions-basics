import math
a = int(input("enter a value : "))

try :
    b = math.sqrt(a)
    print(b)
except Exception as e :
    print(f"cant find the square root as there is a '{e}'")