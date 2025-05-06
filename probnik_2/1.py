from itertools import permutations

a = '27 1347 256 26 36 345 12'.split()
s = 'АБ АВ БВ ВД ВГ ГЕ ДЕ ГЕ ГК ЕК'.split()

print('1 2 3 4 5 6 7')

for p in permutations('АБВДЕГК'):
    if all(str(p.index(x)+1) in a[p.index(y)] for x,y in s):
        print(*p)