#1 Write a program "count_digits.py" to print the number of digits in the given number.

n = input("enter num:")
c = 0
for i in n:
    if i.isdigit():
        c+=1
print(f"the number of digit in the given number is",c)
