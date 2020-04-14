# sets
# unique, unordered and unchangeable elements

# basics
primes = {2,3,5,7,11}

x = 5 in primes
print(x)

# sets contains unique and unordered elements
# therefore 'set' object does not support indexing
alphabet = {'b','c','a','b'}
print(alphabet)

# set operators
s1 = {1,2,3}
s2 = {2,4,6}

s3 = s1 - s2    # difference
print(s3)

s4 = s1 | s2    # union
print(s4)

s5 = s1 & s2    # intersection
print(s5)

# set methods
s1.remove(1)
s1.remove(3)
print(s1)
s2.add(8)
print(s2)

# subset
r = s1 < s2
print(r)

# frozen sets
# frozen sets are immutable, therefore they can be used as keys in dictionaries or as elements in sets
s = {1,2,3}
l = [2,4,6]
fs = frozenset(s)
fl = frozenset(l)
kv = [[fs,0],[fl,1]]
d = dict(kv)
print(d)

