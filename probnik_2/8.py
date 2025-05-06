from itertools import *
c=0
for x in product('0123456789ABCDEF', repeat = 4):
    w = ''.join(x)
    s = ''
    for i in w:
        if i in '02468ACE':
            s += 'g'
        if i in '13579BDF':
            s += 'f'
    if x[0] != '0':
        if x.count('9') == 1:
            if 'gg' not in s and 'ff' not in s:
                c+=1

print(c)