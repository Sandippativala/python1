# 6)find the student from CS department where the roll number may be in capital or small case letters.

roll = input("enter roll number :-")
r = roll[0:2]
if len(roll) == 6:
    if r == "cs" or r == "Cs" or r == "cS" or r == "CS" : #computer science department.
        print("valid roll number",roll)
        
    else:
        print("roll enter only cs roll number department")
        
else:
    print("please enter valid roll number")
