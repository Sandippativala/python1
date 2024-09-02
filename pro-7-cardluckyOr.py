# 7)to read a card as input and output if the card is lucky or not

#card = ["J","Q","K","A"] 
#card = ("J","Q","K","A")
card = {"J","Q","K","A"}
n = input("enter your card :-").upper()
lucky = False
for i in card:
    if i == n: #condition
        lucky = True
        break
if lucky:
    print("lucky card.")
else:
    print("unlucky card.")
