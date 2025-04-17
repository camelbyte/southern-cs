import random
import modules.math_functions as mf 

myset = {"apple", "banana", "cherry"}

print(myset)

num = random.randint(1, 100)
print(num)

b = ascii(num)
print(b)

u = [{1, 2, 3, 4, 5, 6, 7, 8, 9}]
print(type(u))

for x in range(num):
    r = chr(x)
    print(r)

for e in enumerate(range(num)):
    print(e)
    

for i in range(len(u)):
    print(hash(i))
    print(ascii(i))
    print(oct(i))
    print(bin(i))
    print(hex(i))
    print(chr(i))

    
# imported my math_functions module and demonstrating it here:

print(mf.multiply(4, 5))

e = mf.square_root(5)

x = mf.multiply(e, 5)

print(x)
