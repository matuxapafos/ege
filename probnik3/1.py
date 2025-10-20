from itertools import *

a = '236 1457 14 238 269 15 289 479 578'.split()
s = 'АБ АК АИ БК БВ КМ ИМ ИЕ ЕД ДМ ДГ ГВ ВМ'.split()

print('1 2 3 4 5 6 7 8 9')
for p in permutations('АБВГДЕИМК'):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x,y in s):
        print(*p)