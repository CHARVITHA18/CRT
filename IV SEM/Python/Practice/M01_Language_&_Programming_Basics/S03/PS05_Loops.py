'''
n=int(input())
counter = 0
while n>0:
    n//=10
    counter+=1
print(counter)

i=0
while i<=n:
    print(i)
    i+=1

n=int(input())
for i in range(n):
    print("hello world")

while n<0:
    print('hello world!')
    n+=1

n=list(map(int,input().split()))
c=0
for i in range(0,len(n),1):
    c=n[i]**2
    print(c,end=' ')

n=list(map(int,input().split()))
c=0
for i in range(0,len(n,1)):
    if n[i]%2==0:
        c.append(n[i])
print(c)

n=input()
count=0
for i in n:
    if i in 'aeiouAEIOU':
        count += 1
print(count)
'''

