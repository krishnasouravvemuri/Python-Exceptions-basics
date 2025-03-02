a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))

try : 
    c = a/b
    print(c)

except Exception as e:
    print(f" '{e}' is the error encountered")