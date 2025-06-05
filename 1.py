# from itertools import *
#
#
# a = '234 136 12 157 467 25 45'.split()
# s = 'fb bd fd da ae ec cg ge gf'.split()
#
# print('1 2 3 4 5 6 7')
#
# for p in permutations('fbdaecg'):
#     if all(str(p.index(x) + 1) in a[p.index(y)] for x,y in s):
#         print(*p)

# from itertools import *
#
# a = '235 14 1456 236 1367 3457 56'.split()
# s = 'рк кп рт тп рс ст тл лс пл лм мс'.split()
#
# print('1 2 3 4 5 6 7')
# for p in permutations('ркптлсм'):
#     if all(str(p.index(x) + 1) in a[p.index(y)] for x,y in s):
#         print(*p)

from itertools import *

a = '458 568 567 17 1238 2378 346 1256'.split()
s = 'fg ge eh hc cf fa ca ad de db bc bh'.split()

print('1 2 3 4 5 6 7 8')
for p in permutations('fgedbhca'):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x,y in s):
        print(*p)