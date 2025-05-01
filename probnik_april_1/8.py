# from itertools import *
# k = 0
# for x in product('01234567', repeat = 6):
#     s = ''
#     w = ''.join(x)
#     for i in w:
#         if i in '0246':
#             s += 'g'
#         if i in '1357':
#             s += 'f'
#
#     if w[0] != '0':
#         if w.count('3') == 0:
#             if len(set(w)) == len(w):
#                 if 'gg' in s:
#                     k += 1
# print(k)

from itertools import *
k = 0
c = 0
for x in product('ьрплеа', repeat = 5):
    k += 1

    w = ''.join(x)
    print(w)
    
    if k <= 387:
        if w[0] == 'ь':
            c += 1
print(c)

