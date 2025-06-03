from math import prod

c = 0
for lines in open('9_3.txt'):
    a = [int(x) for x in lines.split()]
    if prod(a) > sum(a):
        c += 1
print(c)