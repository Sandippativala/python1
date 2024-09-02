#find birthdays in a month using dictionary birthdays in DD/MM/YY format.

birthdays = {"krunal" : "10/08/04" , 
             "sandip" : "31/08/04" , 
             "darshan" : "05/07/04" ,
             "dhruvraj" : "10/04/04" ,
             "tushar" : "30/05/04" }

month = input("enter month :-") #enter month ex 01,02,03.

if month == "01" or month == "02" or month == "03" or :
    for x,y in birthdays.items():
        if y[3:5] == month:
         print(x)
        else:
           print("birthdays not find.")
else:
    print("please enter valid month")