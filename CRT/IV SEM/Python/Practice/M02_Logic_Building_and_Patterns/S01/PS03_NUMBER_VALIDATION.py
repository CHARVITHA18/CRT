#1. write a pythin for the factorial of a number 
'''
n=int(input())
fac=1
if (n<0):
    print("Doesn't Exist");
elif(n==0):
    print(1)
else:
    for i in range(1,n+1):
        fac=fac*i
    print(f"The factorial of {n} is {fac}")

#2. write a pythin for the factorial of a number 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter Number : "))
if (num<0):
    print("Dosen't Exist")
print(f"The factorial of {num} is {factorial(num)}")

# 3.Armstrong Number
#153==>1,5,3==>(1**3)+(5**3)+(3**3)==>153
def is_armstrong(num):
    original_num = num
    n = len(str(num))
    armstrong_sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** n
        temp //= 10
        
    return armstrong_sum == original_num

test_num = 153
print(is_armstrong(test_num))




#4.Prime number or not

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 17
print(is_prime(n))

#palindrome
def is_palindrome(num):
    if num < 0:
        return False
        
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
        
    return original == reversed_num

test_val = 121
print(is_palindrome(test_val))

#rev interger
def reverse_integer(n):
    reversed_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n //= 10
        
    return reversed_num * sign

test_num = 12345
print(reverse_integer(test_num)) # Output: 54321


#prime number within a range

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Example: Primes between 10 and 50
print(find_primes_in_range(10, 50))


#Monotonic of an array"
#ex:
#1,2,3,4,5==>Montonic
#5,4,3,2,1,==>Monotonic
#5,4,8,6,2,1==>Not Mnotonic
#10,5,6,25,45==>Not monotonic

def is_monotonic(arr):
    inc=True#increasing
    dec=True
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            inc=False
        if arr[i]>arr[i-1]:
            dec=False
    return  inc or dec
u_i=input("Enter here: ")
s_l=u_i.split()
nums=[]
for item in s_l:
    nums.append(int(item))
if is_monotonic(nums):
    print("Monotonic")
else:
    print("Not Monotonic")

#reversing a number

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n //= 10
    return reversed_num

print(reverse_number(12345))


#Roman to interger List or dictonary
def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
            total -= roman_dict[s[i]]
        else:
            total += roman_dict[s[i]]
    return total

print(roman_to_int("MCMXCIV")) 

#Happy Number:ex:25=>2**2+5**2 unitl it become s1

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        n = total
    return n == 1

print(is_happy(19)) 
print(is_happy(25)) 


'''