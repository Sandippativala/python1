# print fibonacci sequence.

n = int(input("enter number :-"))

a = 0
b = 1

while n > 0:
    print(a)
    sum = a + b
    a = b
    b = sum
    n = n -1