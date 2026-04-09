'''
def Natural_sum(n):
    s=0
    for  i in range(n,0,-1):
        s+=i
    return s
#n(n+1)/2
print(Natural_sum(5))
print(Natural_sum(10))

def natural_sum1(n):
    if n==1:
        return 1

    else:
        return n + natural_sum1(n-1)
print(natural_sum1(5))
print(natural_sum1(10))

def factorial(n):
    if n<0:
        return "undefineed"
    elif n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(factorial(n))


def fibonacci(n):
    if n<=0:
        return n
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
print(fibonacci(n))
'''
#Gcd of 2 numbers
def GCD(a,b):
    if b==0:
        return a 
    else:
        return GCD(b,a%b)
print(GCD(4,10))
