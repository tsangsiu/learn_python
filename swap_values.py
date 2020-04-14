# to swap the values of a and b without an additional variable

# old way
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# the python way
a = 10
b = 20
a,b = b,a
print(a)
print(b)