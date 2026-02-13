'''Data types
1 fundamental 
  int
  float
  complex
  boolean
  string
2 collection
  list
  tuple
  set
  dictionary
'''
x=12
y=12.45
z=4+5j
print(x,type(x))
print(y,type(y))
print(z,type(z))

f1 = 3e2
f2 = 4E3
print(f1,type(f1))
print(f2,type(f2))

c1 = 4 + 5j
c2 = complex(2,-3)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)


print("c1.real" , c1.real ) # to get real part name.real
print("c1.imag" , c1.imag) # to get img part name.img
print("c2.real" , c2.real)
print("c2.imag" , c2.imag)

s = "Python"
print(s[2])
print(s[ : : ])
print(s[ : : 2])
print(s[ : : -1])
print(s[0:6:-2])
