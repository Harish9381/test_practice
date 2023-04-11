#The US Constitution says you must be a natural born citizen *and* at least 35 years old. Write a function "can_run_for_president" which takes two arguments `age` and `is_natural_born_citizen` and check if the person is  eligible to run for president in the US?
# Test Scenarios:
# 	print(can_run_for_president(19, True))
# 	print(can_run_for_president(55, False))
# 	print(can_run_for_president(55, True))

def can_run_for_president(age,natural_born_citizen):
    if(age > 35 and natural_born_citizen):
        return "eligible"
    else:
        return "not eligible"
res = can_run_for_president(19,True)
res1 = can_run_for_president(55,False)
res2 = can_run_for_president(55,True)
print(res,res1,res2)