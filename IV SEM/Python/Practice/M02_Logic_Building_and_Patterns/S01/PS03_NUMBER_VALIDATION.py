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
n=int(input())
s_n=str(num)
s_d=len(s_n)




#4.Prime number or not

#palindrome
#rev interger

#prime number within a range
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
#Roman to interger List or dictonary
roman = input("Enter a roman numberal: ").upper()
values = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 
}

#Happy Number:ex:25=>2**2+5**2 unitl it become s1
'''