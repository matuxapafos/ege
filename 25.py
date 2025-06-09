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
# from fnmatch import *
# def f(x):
#     divs = set()
#     for d in range(1,int(x**0.5) + 1):
#         if x % d == 0:
#
#             if d % 2 ==0: divs.add(d)
#             if (x//d) % 2 ==0:divs.add(x//d)
#
#     return divs
#
#
#
# for x in range(65001,10000000000):
#     if fnmatch(str(x), '6*97*5?'):
#         divs = f(x)
#         if len(divs) >= 4:
#             print(x,sum(divs))

from fnmatch import *

for x in range(1923,10**8+1,1923):
    if fnmatch(str(x), '1*2??76'):
        print(x, x // 1923)
