'''set:
1.use {} to create a set
2.set does not allow duplicates
3.set is undefined
4.set is mutable
5.set is unordered
6.set is heterogenous
s={1,True,10,12.45,10,9+5j}
print(s,type(s))
print(s[3])

#Adding elements
A={1,2,3}
B={3,4,5}
A.add(4)
B.update({6,7})
print(A,B)

#Remove elemnts
A.pop()
print(A)
A.remove()


nums = [3,0,1]
n=len(nums)
res=set(range(n+1))
print(res-set(nums))
print(res.pop())

s=(n*(n+1))//2
print(s-sum(nums))

Tuples:
1->slicing of tuple
2->Repetion of tuples
3->immutable



t=(10,23)
t[0]=50 #error immutable
print(t)

t=(10,23,50,12,45,32,48)
t2=("sai","kalyani","krishna")
print(t[0])
print(t[-1])
print(t+t2)
print(t,t2)#nested
print(t*5)#repetition
print(t[1:4])#slicing
print(t[:5])
print(t[:-1])
del t

'''

d={"a":'sai'}
print(d)
d2=dict(a='sai',b='Kalyani',c='Krishna')
print(d2)
print(d2['a'])
print(d2.get('b'))
print(d2.keys)
print(d2.values)
#print(d2={'age':25})

deleting of dictanory:
del-->delete
pop()->removes key returns ValueError
popitem()-> removes last inserted key value pair and return it a 
clear()->remove entire dict 