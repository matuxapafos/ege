# from itertools import *
# list=[]
# k = 0

# for x in product('0123456789ABCDEF', repeat=4):
#     s1 = 0
#     s2 = 0
#     res = ''
#     w = ''.join(x)
#     if x[0] != '0':
#         for i in w:
#             if i in "13579BDF":
#                 res += "g"
#                 s1 += int(i,16)
#             else:
#                 res += 'x'
#                 s2 += int(i,16)
            
#         if res.count('g') == 2 and res.count('x') == 2:
#             if s1 == s2:
#                 if len(set(w)) == len(w):
#                     k +=1
                    
# print(k)

# from itertools import *
# k = 0
# for x in product('0123456789AB',repeat=7):
#     w = ''.join(x)
#     res = ''
#     if x[0] != '0':
#         for i in w:
#             if int(i,12) % 3 == 0:
#                 res += 'g'
#             else:
#                 res += 'x'
#         if res == 'gxgxgxg' or res == 'xgxgxgx':
#             k+=1
# print(k)

# from itertools import *

# k = 0
# for x in product('абдежнотухчю', repeat=12):
#     w = ''.join(x)
#     res = ''
#     for i in w:
#         if i in 'аеоую':
#             res+='x'
#         else:
#             res+='g'
#     if 'xxxxx' not in res:
#         k+=1
# print(k)
    
# from itertools import *
# c = 0
# for x in product('0123456789ABCDE', repeat=5):
#     k = 0
#     w = ''.join(x)
#     if x[0] != '0':
#         if w.count('8') == 1:
#             for i in w:
#                 if int(i,15) > 9:
#                     k += 1
#             if k >= 2:
#                 c+=1
#
# print(c)

# from itertools import *
#
# c = 0
# for x in product('0123456789ABCDEF', repeat = 4):
#     w = ''.join(x)
#     f = ''
#     for i in w:
#         if i in '02468ACE':
#             f += 'g'
#         else:
#             f += 'e'
#     if w[0] != '0':
#         if w.count('9') == 1:
#             if 'gg' not in f and 'ee' not in f:
#                  c += 1
#
# print(c)

# from itertools import *
# c = 0
# for x in product('АГДЕПР', repeat = 5):
#     if x.count('Г') == 1:
#         if x[0] != 'А' and x[-1] != 'Е':
#             c += 1
#
# print(c)

# from itertools import *
# c = 0
# for x in product('0123456', repeat = 6):
#     w = ''.join(x)
#     f = ''
#     for i in w:
#         if i in '0246':
#             f += 'g'
#         else:
#             f += 'e'
#     if w[0] != '0':
#         if int(x[-1],7) >= 4:
#             if f.count('g') == f.count('e'):
#                 c += 1
# print(c)

from itertools import *
c = 0
for x in product('01234567', repeat = 5):
    w = ''.join(x)
    f = ''
    for i in w:
        if i == '6':
            f += 'g'
        elif i in '1357':
            f += 'e'
        else:
            f += 'd'
    if w[0] != '0':
        if w.count('6') == 1:
            if 'ge' not in f and 'eg' not in f:
                c += 1
print(c)