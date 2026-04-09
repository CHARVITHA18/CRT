'''
Arrays:
1. List ==> Built-in Data Structure
        1. use [] to create a list
        2. List is mutable
        3. List is heterogenous
        4. List is indexed
        5.List is Ordered
        6.List allows duplicate values
2. Array using array module
3.Array using numpy module

li = [1,12.5,True,1,"Python",2+5j]
print(li,type(li))

#NO.of elements len()
print(len(li))

#UPdate
li[2]=False
print(li)

#Addding element ==> append() and insert() method we can only initialze only 1 at a time
li.append(100)
print(li)

#insert
li.insert(1,100)
print(li)

li.insert(20,200)
print(li)

li.insert(-20,300)
print(li)

#extend will add 2 or more items at a time
li.extend([300,400,500])
print(li)

#pop removes an element
li.pop()
print(li)

li.pop(1)
print(li)

#li.pop(20)
#print(li)

# Remove  removes the first occurrence of the value 100 from the list.
li.remove(100)
print(li)

 
#clear clears everything
 
li.clear()
print(li)

#copy if u do any operation it will not effect

l1=[1,2,3]
l2=l1
l3=l1.copy()
print(l1,l2,l3)

l1.append(4)
print(l1,l2,l3)
#here when we use copy () any opeation we do will not modify if we use copy operator whereas if u copy using assignment operators it will modify accordinlyy
'''

from array import array 
arr = array('i',[10,20,30])
print(arr,type(arr))

#arr.append(12.45)

import random 
li=[1,2,3]
li=random.randint(0,3)
#print(i,li[i])