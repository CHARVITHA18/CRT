'''
Optimization: process of modifying the code to reduce the time compexity
Brute Force --. trying of all possible combinations
optimal solution --. needs thinking,low complexity
Optimization Basics : Making the sution 

a=[10,20,30,40,52]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i]+a[j])  #O(n^2)

a=[10,20,30,40,52]
for num in a:
    print(num+num)#O(n)

why it is import
improve code speed
reduce memory usage


-->Find sum of numbers in Arr 

arr=[10,20,30,40,50]
arr1=sum(arr)
print(arr1)

arr=[10,20,30,40,50]
arr1=0
for i  in range(len(arr)):
    arr1+=arr[i]
print(arr1)

-->find maximum element in a list

'''
arr=[10,20,30,40,50]
arr1=max(arr)
print(arr1)

arr=[10,20,30,40,50]
