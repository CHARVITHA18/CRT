'''
Square star pattern 
n=4
* * * * 
* * * * 
* * * *
* * * *



n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print() #nextLine



Right Angle Triangle
n=4
*  1
* *  2
* * *  3
* * * *  4

n=int(input())
for i in range(1,n+1): #1 to 5 range
    for j in range(i): #i range
        print("*",end=" ")
    print()

inverted Triange
* * * *
* * *
* *
*

n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

repeated num tri
1
2 2
3 3 3
4 4 4 4
    
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    
Number triangel 
1
1 2
1 2 3
1 2 3 4




n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

    
Alphabet triangle
A ==>65
A B 
A B C
A B C D
    ORD CHR

n=int(input())
for i in range(1,n+1):
    ch=65
    for j in range(i):
        print(chr(ch+j),end=" ")
    print()

 
Floyd Triange
1
2 3  
4 5 6 
7 8 9 10

Hollow Square
* * * * 4 at 0 sp
*     * 2 st 2 sp
*     * 2 st 2 sp
* * * * 4 st 0 sp


n=int(input())

for i in range(n):
    for j in range
       '''
