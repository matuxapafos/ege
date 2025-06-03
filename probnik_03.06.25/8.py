from itertools import *
c = 0
for x in product('01234567',repeat = 5):
    if x[0] != '0':
        if x[0] not in '1357':
            if x[-1] not in '26':
                if x.count('7') <= 2:
                    c += 1
print(c)