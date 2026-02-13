#Number Series : Sequestial order of numbers in  a particular 
# 1 printn natural numbers
'''
n=int(input())
for i in range(n+1):
    print(i,end = " ")
   
# print n even numbers
n=int(input())
for i in range(,n+1):
    if(i%2==0):
        print(i,end=" ")

for i in range(2,n+1,2):   
    print(i)    
# print n odd numbers
n=int(input())
for i in range(0,n+1):
    if i%2!=0:
        print(i,end=" ")

for i in range(1,n+1,1):
    print(i)
 
#pritn n fibanoci series
n=int(input())
a=0
b=1
for i in range(n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    
#print n fibannoci using while loop
# multiplication table
n=int(input())
for i in range(0,11):
    print(n , "*" , i , "=" , n*i)

#print n squares and cubes of n natural number
n=int(input())
print(n**2)
print(n**3)
  
#print n fibannoci using while loop


#alternative number series : 1 -2,,3,-4,5,-6,.......
n=int(input())
for i in range(1,n+1):
    if (i%2==0):
        print(-i,end=" ")
    else:
        print(i,end=" ")5

'''

#1,2,4,7,11,16,22   diff is n naturanl numbers staring ewith 1 
n = int(input("Enter number of terms: "))
dif= 1  
for i in range(n):
    print(dif, end=" ")
    dif =dif + (i + 1)

#1,2,6,24,120....
