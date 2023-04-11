 # Write a function ‘select_second’ with one argument ‘L’ which is a list to return the second element of the given list. If the list has no second element, it should return None.
def select_second_element(l):
    for i in range(len(l)):
        if (len(l) > 0):
            return(l[1])
        else:
            return None
res = select_second_element([1,2,3,4,5])   
print(res)     