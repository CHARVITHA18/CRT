'''
Pascal Triangle
n=5
output:
1
1 1
1 2 1
1 3 3 1 
1 4 6 4 1

n=int(input())
for i in range(n):
    num= 1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()



2.Butterfly pattern 
n=4
output: 
*      *
**    ** 
***  ***
********       *      *
********       **    **
***  ***       ***  ***
**    **       ********
*      *

'''

n=int(input())
for i in range(1,n+1):
    print()


