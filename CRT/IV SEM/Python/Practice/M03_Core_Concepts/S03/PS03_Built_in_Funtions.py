
'''
1)Find Largest Number (using max()) --> largest value in a list 

arr=[10,20,30,46,49,30]
print(max(arr))
2) Check Palindrome (using reversed() & join())

word='madam'
if word == "".join(reversed(word)):
    print("palindrome")
else:
    print("not a palindrome")
3)count even numbers(using filter()) --> filters elements based on a condition 

arr=[10,20,30,40,59]
res=list(filter(lambda x:x%2==0,arr)
print(res)

4)Remove Duplicates (using(set()))unique collection of data

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

5)sum of digits (using sum()) --> sums up the digits of a number

num = 1234
digit_sum = sum(int(digit) for digit in str(num))
print(digit_sum)

6)sort words alphabetically (using sorted()) --> sorts a iist of words in alphabetical order

words = ["banana", "apple", "cherry", "mango"]
sorted_words = sorted(words)
print(sorted_words)

7)find common elements (using(set()))

a = set([10, 20, 30, 40, 50])
b = set([60, 70, 80, 90, 10])

common_elements = a.intersection(b)
print(common_elements)  

8)Index with value (using enumerate()) --> adds a index to each elementwhile iteral

fruits = ["apple", "banana", "mango"]
for index, value in enumerate(fruits):
    print(index, value)

9)pair two lists (using zip()) --> combines multiple iterals elem-wise

names = ["Ram", "Shyam", "Mohan"]
marks = [90, 85, 88]
paired = zip(names, marks)
print(list(paired))


10)find second largest element(using sorted()) -->sorts the listnd returns the second largest element

numbers = [10, 20, 5, 40, 30]
sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
print(second_largest)

'''


