from itertools import *
k = 0
for x in product('01234567', repeat = 6):
    s = ''
    w = ''.join(x)
    for i in w:
        if i in '0246':
            s += 'g'
        if i in '1357':
            s += 'f'

    if w[0] != '0':
        if w.count('3') == 0:
            if len(set(w)) == len(w):
                if 'gg' in s:
                    k += 1
print(k)
