#  Define a function “sign” which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.  
def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0
res = sign(1)
res1 = sign (-5)
res2 = sign(0)  
print(res,res1,res2)  