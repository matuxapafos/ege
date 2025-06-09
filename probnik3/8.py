from itertools import *
count = 0
for x in product('012345', repeat = 7):
    w = ''.join(x)

    if w[0] != '0':
        w = w.replace('0', 'c').replace('4', 'c')
        if w.count('2') == 1 and '2c' not in w and 'c2' not in w:
            count += 1
print(count)