from itertools import *

def f(x,y,z,w):
    return (not(x <= y )) or (z <= w) or (not z)

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
    t = (
        (x1,0,x2,0,0),
        (1,x3,x4,x5,0),
        (0,1,x6,x7,0)
    )
    if len(t)==len(set(t)):
        for p in permutations('xyzw',r = 4):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p)