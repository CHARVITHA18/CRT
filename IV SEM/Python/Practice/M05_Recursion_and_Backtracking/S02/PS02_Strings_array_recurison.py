
'''
#Caluculating sum of all elements in a list
def Array_Sum(nums):
    s=0
    for i in range(len(nums)):
        s+=nums[i]
    return s
print(Array_Sum([10,20,30,40]))


def Array_Sum1(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[-1]+Array_Sum1(nums[:-1])
print(Array_Sum1([10,20,30,40]))



#REVERSING A LIST
def reversing_array(nums,i,j):

    if i>=j:
        return
    nums[i],nums[j]=nums[j],nums[i]
    reversing_array(nums,i+1,j-1)
    return nums
print(reversing_array([1,2,3,4,5],0,4))

'''

#reverse a string with recursive calls
def reverse_str(s):
    pass
print(reverse_str("python")) 