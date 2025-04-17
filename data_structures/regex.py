import re

string = "The quick brown fox jumps over the lazy dog"

look_for = "fox"

if re.findall(look_for, string):
    print(f"Found '{look_for}'")
else:
    print(f"Did not find '{look_for}'")

look_for = "wolf"

if re.findall(look_for, string):
    print(f"Found '{look_for}'")
else:
    print(f"Did not find '{look_for}'")

l = ["sam", "samantha", "cat\n", "dog", "wolf\n", "bear", "lion"]

dot = [re.findall(".", look_for)]
print(dot)

for i in l:
    print(i)
