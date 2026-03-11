#Leetcode
'''
1.Running Sum of 1d Array

n=[1,2,3,4]
res=[]
s=0
for ele in n:
    s=s+ele
    res.append(s)
print(res)

a=[1,2,3,4]
sum=0
for i in range(len(a)):
    sum=sum+a[i]
    a[i]=sum
print(a)        

2.Contains Duplicate

n=[1,2,3,1]
if len(n)!=len(set(n)):
    print("true")
else:
    print("False")

3.Richest Customer Wealth

a=[[1,2,3],[3,2,1]]
max_wealth=0
for customer in a:
    total=sum(customer)
    if total>max_wealth:
        max_wealth=total
print(max_wealth)

1929
1470
1
27
66
121

66.Plus One
'''
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits