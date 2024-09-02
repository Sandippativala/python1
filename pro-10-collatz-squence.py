'''collatz squence 
 1.for even number divide by 2.
 2.for odd number, multiply by 3 and add 1.
 3.repeat above steps, until it becomes 1.'''

num = int(input("enter number :-"))

while(num != 1):
    if num % 2 == 0:
        num //= 2
    else:
        num = num *3+1
    print(num)