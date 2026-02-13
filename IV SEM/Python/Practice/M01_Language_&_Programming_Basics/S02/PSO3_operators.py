x = 13
y = 5
print(x&y)
print(x|y)
print(x^y)
print(x<<2)
print(x>>2)

#MEMBERSHIP OPERATORS => in , not in
print("on" in "Python")
print(100 in [10,20,30,40])

#IDENTITY PEROTORS ==> is , not is

#in python for memory allocation they use reference counting
#in java for memory alloctaion they use mark and sweep

a = 10
b = 20
c = 10
print(a is b)
print(a is c)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)
print(id(l1) , id(l2))