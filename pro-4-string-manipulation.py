# 4).word shuffle using string manipulation

s = "my name is krunal pativala"
name =  s[0:11]  #my name is 
lname = s[18:len(s)] #pativala
fname = s[10:18] #krunal
n = s[3:7] #name

print(name + lname)
print(name + fname)
print(lname + fname)
print(n + fname)
print(name + fname + lname)
#print(s[0:11] + s[18:len(s)])