#13 exact change.
price = int(input("enter price :-"))
demo1 = int(input("enter coin1 :-"))
demo2 = int(input("enter coin2 :-"))
demo3 = int(input("enter coin3 :-"))
f = 0 

for d1 in range(0,(price // demo1) + 1):
    for d2 in range(0,(price // demo2) + 1):
        for d3 in range(0,(price // demo3) + 1):
            if d1*demo1 + d2*demo2 + d3*demo3 == price:
                print(d1 , d2 , d3)
                f = 1
if f == 0:
    print("no match found.")
        