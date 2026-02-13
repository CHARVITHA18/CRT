'''


li=[1,2,3,4,5]
#output=[2,4,6,8,10]
res=[]
for i in li:
    res.append(i*2)
print(res)
print([i%2==0 for i in li])   #comprehisions

li=[1,2,3,4,5]
#output=[2,4]
res=[]
for i in li:
    if i%2==0:
        res.append(i)
print(res)

#[]for loop before foor loop i%2 condition  
print([i for i in li  if i%2==0])#list
print(tuple(i for i in li  if i%2==0))#tuple
print({i:i*2 for i in li  if i%2==0})#dictonary


li1=['a','b','c']
li2=['d','e','f']

1.Pyramid
n=4
output:
   *
  * *
 * * *
* * * * 

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

2.inverse pyramid
* * * *
 * * *
  * *
   *
'''
n=int(input())
for


