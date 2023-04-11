#1. Write a function named type_check that takes two parameters and it should return True if both parameters are of the same data type, and False otherwise.
#For example, calling type_check(1, 2) should return True, while calling type_check("a", 1) should return False.

def type_check(a,b):
    if type(a) == type(b):
        return ("True")
    else:
        return ("False")
print(type_check("hari",24))
print(type_check(12.24,34.25))    
