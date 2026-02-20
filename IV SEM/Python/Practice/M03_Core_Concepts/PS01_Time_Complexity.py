def Linear_Search(elements,target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1
print(Linear_Search([12,45,78,69,32],12)) # best case
print(Linear_Search([12,45,78,69,32],78))#avg case
print(Linear_Search([12,45,78,69,32],32))#worst case
