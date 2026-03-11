''''
def Linear_Search(elements,target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1
print(Linear_Search([12,45,78,69,32],12)) # best case O(1)
print(Linear_Search([12,45,78,69,32],78))#avg case O(n)
print(Linear_Search([12,45,78,69,32],32))#worst case O(n)


LIST
[]
ADD==> append()   insert()   extend()
remove==> pop() remove() clear()
sort()=>reverse=True
reverse()
index()
copy()
count()
max() 
min()
len()
list()
sorted()
reversed()

'''
nums=[1,2,3,4]

if nums==list(set(nums)):
    print("True")
else:
    print("False")


