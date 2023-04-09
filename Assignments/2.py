#2 Find the faculty with highest pass percentage (> 40%) 

import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

sub_faculty = {
    'Maths' : 'Murali Krishna',
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Social' : 'Krishna Reddy',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi'
}

pass_mark = {}

with open('C:/Users/HP/OneDrive/Desktop/exam/test_practice/Assignments/student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for marks in data:
        if int(marks['Telugu']) > 40:
            Telugu += 1
        if int(marks['English']) > 40:
            English += 1
        if int(marks['Maths']) > 40:
            Maths += 1
        if int(marks['Physics']) > 40:
            Physics += 1
        if int(marks['Chemistry']) > 40:
            Chemistry += 1
        if int(marks['Social']) > 40:
            Social += 1
    
    pass_mark['Telugu'] = Telugu
    pass_mark['English'] = English
    pass_mark['Maths'] = Maths
    pass_mark['Physics'] = Physics
    pass_mark['Chemistry'] = Chemistry
    pass_mark['Social'] = Social

print(pass_mark)
pass_perc = max(pass_mark.items(),key=lambda x:x[1])
print(f"Highest Pass Percentage is {pass_perc}")
faculty = (pass_perc); (sub,marks) = faculty
print(pass_perc)
print(sub_faculty[sub])