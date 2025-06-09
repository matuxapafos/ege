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

# from functools import *
# import sys
# sys.setrecursionlimit(5000)
# c = 0
# @lru_cache(None)
# def f(n):
#     if n == 0:
#         return 0
#     if n > 0 and n % 2 == 0:
#         return f(n//2)
#     if  n % 2 != 0:
#         return 1+f(n-1)
#
# for n in range(1,501):
#     if f(n) == 8:
#         c+= 1
# print(c)
# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n % 2 == 0: return n + f(n-1)
#     if n % 2 != 0 and n > 1: return 2 * f(n-2)
#
# for n in range(1,2000): f(n)
#
# print(f(26))

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n == 0: return 1
#     if n == 1: return 3
#     if n == 2: return  2
#     if n > 2: return f(n-1) * f(n-3)
#
# for n in range(2,7): f(n)
#
# print(f(7))

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n <= 3:return 1
#     if n>3: return (n+3) * f(n-2)
#
# for n in range(3,3000): f(n)
#
# print(f(2028)/f(2024))


# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 3: return 2**1024
#     if n >2: return 2*n + 3 + f(n-2)
#
# for n in range(1,3000):
#     f(n)
#
# print(f(4048) - f(16))

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n <3: return 2
#     if n > 2 and n % 2 ==0: return 2*f(n-2)-f(n-1)+2
#     if n>2 and n % 2 !=0: return 2*f(n-1) + f(n-2) - 2
#
# for n in range(1, 200): f(n)
#
# print(f(170))
f = {}

# for n in range(-20,5000):
#     if n == 1: f[n] == 1

