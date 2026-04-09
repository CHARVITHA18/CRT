#STring is a collection of characters enclosed in quotes
#string is immutable
'''
s='python'
s1="python"
s2=

python 
is
intersting 


print(s1+s2)#concatination
print(s1*2)#repetionn
print("on" in s1)
s[1]='z'

#Built-In Functions
#length
s='python'
print(len(s))
print(max(s))
print(min(s))
print(max("abc123ABC"))
s.replace("y",'Y')
print(s)
#print(dir(str)) IN BULID MEATHODS OF STR
print(s.find("on"))
print(s.find("xyz"))

#revere a string without using slice operator
s=input()
rs=""
for ch in s:
    rs=ch+rs
if s==rs:
    print(rs+" is palindrome ")
else:
    print("Not a palindrome")
    '''
#check ehrether  it is anangram or not
s1=input().lower()
s2=input().lower()
if sorted(s1)==sorted(s2):
    print("YES!! IT IS ANAGRAM")
else:
    print("NO!!") 

from Collectons import Counter
s1=input()
s2=input()
print("Anagrams" if Counter(s1)==Counter(s2) else "not anagram")           