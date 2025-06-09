# from functools import lru_cache
#
# def f(n):
#     if n == 1: return 1
#     if n > 1 and n % 2 !=0: return 3*n + f(n-2)
#     if n > 1 and n % 2 ==0: return 4 * f(n/2)
#
# for n in range(1,50):
#     f(n)
# print(f(42))

f = {}
for n in range(1,100):
    if n == 1: f[n] = 1
    if n > 1 and n % 2 !=0: f[n] = 3 * n + f[n-2]
    if n > 1 and n % 2 == 0: f[n] = 4 * f[n/2]
print(f[42])