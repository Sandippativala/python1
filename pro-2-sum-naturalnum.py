# 2).find the sum of the first n nutural number.

n = int(input("enter number :-")) #user input
if n >= 0:
    sum = n * (n+1)/2
    print(sum)
else:
    print("please enter valid number")