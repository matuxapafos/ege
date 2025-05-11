# from functools import *
#
# @lru_cache(None)
# def f(n):
#     sumi = 0
#     for i in str(n):
#         sumi+= int(i)
#     if n < 3:
#         return 1
#     if n > 2 and sumi % 2 == 0: return f(n-1) - f(n-2)
#     if n > 2 and sumi % 2 != 0: return f(n-1) + f(n//2)
#
# for n in range(1,101): f(n)
#
# print(f(100))
#
#
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 0:
#         return g(n) + f(n-1)
#     if n > 2 and n % 2 != 0:
#         return f(n-2) - 2*g(n+1)
#
# def g(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 0:
#         return f(n-3) + f(n-2)
#     if n > 2 and n % 2 != 0:
#         return f(n+1) - g(n-1)
#
# for n in range( 1,200): g(n)
#
# print(g(120))

from functools import *
import sys
sys.setrecursionlimit(5000)
c = 0
@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n//2)
    if  n % 2 != 0:
        return 1+f(n-1)

for n in range(1,501):
    if f(n) == 8:
        c+= 1
print(c)