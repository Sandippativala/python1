#primaliy testing given a positive integer, check if the number is prime or not.

num = int(input("enter number :-"))

is_prime = True
if num > 1:
    for i in range(2,num):
        if num % i == 0: # not prime number
            is_prime = False
            break
if is_prime: #condition True / False
    print("is prime number.")
else:
    print("is not prime number.")