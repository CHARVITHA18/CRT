'''
1)REVERSE AN ARRAY:
a) Using slicing function
b) using reverse()
c) using Loop 

a=[10,23,45,65,1,2,3]
a.sort()
print(a[::-1])


a=[10,23,45,65,1,2,3]
a.sort()
a.reverse()
print(a)

#find min and max ele?
nums = [34, 7, 23, 32, 5, 62]

min_val = min(nums)
max_val = max(nums)

print(f"Min: {min_val}, Max: {max_val}")


#find second largest element
def find_second_largest(nums):
    if len(nums) < 2:
        return None
    
    first = second = float('-inf')
    
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
            
    return second if second != float('-inf') else None


print(find_second_largest(arr)) 

#remove duplicates from array
def remove_duplicates(nums):
    if not nums: return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1  # Length of unique elements

'''
total=sum(nums)
ft=3
for i in range(len(nums)):
    right=total-left
    