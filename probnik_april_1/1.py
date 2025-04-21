from itertools import *
a = '56 4568 78 2578 1246 125 348 2347'.split()
s = 'АЕ АБ БЖ ЖГ БГ АГ ЕГ БД ЖД ДВ ДИ ЖИ ИВ'.split()

print('1 2 3 4 5 6 7 8')
for p in permutations('АЕБЖГИВД'):
    if all(str(p.index(x)+1) in a[p.index(y)] for x,y in s):
        print(*p)



