#1 count the nomber of digits of an number
'''
n=1567
n%10==>Last digit
n//10 ==>quoient


n=int(input())
count=0
for i in range(n):
    if i%10 != 0:
        count += 1
    else:
        break
System.out.println(count);

n=int(input())
temp=n
count=0
while n>0:
    count+=1
    n%=10
print(count)
print(len(str(temp)))


#Find the sum of digits of a number
n=int(input())
s=0
while n>0:
    s+= (n%10)
    n //= 10 
print(s)
'''
# count even and odd
n=int(input())
e=0
c=0
while(n>0):
    if n%2==0:
        e+=1
    else:
        o+=1
print(e)
print(o)

#digital sum from user
# 789 ===> 24 ==> 6
# 12345 ==>15 ==>6

