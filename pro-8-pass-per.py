#find out pass-percentage of a class.

pass_count = 0
n = int(input("Enter number of students: ")) #number of students

if n <= 0:
    print("Number of students must be greater than 0.")
else:
    for i in range(n): #range n
        mark = int(input("Enter mark for student {0} :-".format(i+1)))
        if mark >= 40:
            pass_count = pass_count + 1

    per = (pass_count * 100) / n #passing percentage
    print(per,"% passed")
