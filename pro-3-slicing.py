# 3).extracting fields of a roll number using string indexing and slicing

roll = input("enter roll number :-")

if len(roll) == 5: #len of roll number 5
    r = roll[0:2]  

    r_number = roll[2:5]
    
    print("computer department :-",r)
    print("roll number",r_number)
    print("valid number")
else:
    print("invliad number")