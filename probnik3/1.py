from itertools import *

a = '47 357 2567 16 236 345 123'.split()
s = 'FC CG GA AD DB BF FE BE CE GE'.split()

print('1 2 3 4 5 6 7')
for p in permutations('FCGABDE'):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x,y in s):
        print(*p)