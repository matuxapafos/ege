# from itertools import *
#
# def f(a,b,c,t):
#     return ((not(a)) or (not(b))) and (c <= (not(a))) and (t and (not(a)) or c and (not(b)))
#
# z = ((1, 0, 0, 1, 0),
#      (1, 1, 0, 1, 1),
#      (0,0,0,1,0),
#      (1,0,0,0,1))
# if len(z) == len(set(z)):
#     for p in permutations('abct', r = 4):
#         if all(f(**dict(zip(p,l)))==l[-1] for l in z):
#             print(*p)
#

# from itertools import *
#
# def f(x,y,z,w):
#     return (w or x or y) <= ((y or z)and x or y and (w or z))
#
# for x1,x2,x3,x4,x5 in product([0,1], repeat = 5):
#     t = (
#         (0,0,0,x1,0),
#          (x2,1,1,x3,0),
#          (x4,1,x5,1,0)
#          )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r = 4):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p)

# from itertools import *

# def f(x,y,z):
#     return (not(z)) and x or x and y
#
# t = (
#     (0,0,0,0),
#     (0,0,1,1),
#     (0,1,0,0),
#     (0,1,1,1),
#     (1,0,0,0),
#     (1,0,1,0),
#     (1,1,0,0),
#     (1,1,1,1)
# )
# if len(t) == len(set(t)):
#     for p in permutations('xyz',r = 3):
#         if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#             print(*p)

# from itertools import *
#
# def f(x,y,z,w):
#     return ((x <= y) or (z==x)) and (w <= z)
#
# t = (
#     (0,0,1,1,1),
#     (0,0,1,0,0),
#     (0,1,1,1,0)
# )
#
# if len(t) == len(set(t)):
#     for p in permutations('xyzw', r = 4):
#         if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#             print(*p)

from itertools import *

# def f(a,b,c,d):
#     return ((a and b  == (not c)) and (b and d)
# t = (
#     (1,0,0,0,1),
#     (1,0,1,0,1),
#     (1,0,1,1,1),
#     (1,1,0,0,1)
# )
# if len(t) == len(set(t)):
#     p = 'cadb'
#     if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#         print(*p)

from itertools import *

def f(x,y,z,w):
    return (not((((not w) <= (not y)) <= (not z)) <= x))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1,x2,1,0,1),
        (x3,1,x4,1,1),
        (0,1,x5,0,0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p)
