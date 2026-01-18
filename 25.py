# from fnmatch import *
# for x in range(151,10**9+1,151):
#     if fnmatch(str(x), '2?34?56?8'):
#         print(x, x//151)


# from fnmatch import *
# for x in range(2023, 10**8 + 1,2023):
#     if fnmatch(str(x), '3?1*57'):
#         print(x,x//2023)

# from fnmatch import *
# for x in range(28,10**9+1,28):
#     if fnmatch(str(x), '6323*353?'):
#         print(x, x//28 )

from fnmatch import *
# def f(x):
#     divs = set()
#     for d in range(1,int(x**0.5) + 1):
#         if x % d == 0:
#             divs.add(d)
#             divs.add(x//d)
#     return sorted(divs)
#
# for x in range(1350050,10000000000):
#     a = [i for i in f(x) if i % 100 ==11 and i!= 11]
#     if len(a)>0:
#         print(x,min(a))

#
# from fnmatch import *
#
# for x in range(1923,10**8+1,1923):
#     if fnmatch(str(x), '1*2??76'):
#         print(x, x // 1923)

# import math
#
# a = 100000
# a2 = 999999
# b = [x for x in range(113,1000000,226)]
# c = [3**x for x in range(1,30)]
#
# l = []
# for i in b:
#     for j in c:
#         if (i+j>=a) and (i+j<= a2) and (str(i+j).count('0') == 0):
#             l.append([i+j,round(math.log(j,3))])
#
# print(sorted(l))

import math
a = 1000000
b = [x for x in range(222,10000000,222)]
c = [5**x for x in range(1,20)]

l = []
for i in b:
    for j in c:
        if (i+j>a) and str(i).count('1') == 0 and str(i).count('3') == 0 and str(i).count('5') == 0 and str(i).count('7') == 0 and str(i).count('9') == 0:
            l.append([i+j, round(math.log(j,5))])
print(sorted(l)[:5])