# def f(x):
#     return (x & 57 == 0) or ((x & 23 == 0) <= (not(x & a == 0)))

# for a in range(1,1000):
#     if all(f(x) for x in range(1,100000)):
#         print(a)
#         break

def deli(x,y):
    return x % y == 0

for a in range(1,10000):
    if all((not(deli(x,7) and deli(x,13)) <= (x > a -40)) for x in range(1,10000)):
        print(a)

# def deli(n,m):
#     return n%m==0
# def sumb(s,d):
#     return s + d >0
#
# def f(x,a):
#     return (x+a>=160) or (deli(x,7) <= (not(sumb(x,-17))))
#
# print(min(a for a in range(1,200) if all(f(x,a) for x in range(1,400))))

# def f(x,a):
#     return (x&29 == 0 ) or ((x&11 == 0) <= (not(x&a==0)))
#
# print(min(a for a in range(0,200) if all(f(x,a) for x in range(15,31))))

# def f(x,y,a):
#     return (x + 2*y != 58) or ((a - x>0 ) == (a + y>0))
#
# print(min(a for a in range(1,200) if all(f(x,y,a) for x in range(1,400) for y in range(1,400))))

# def f(x,y,a):
#     return (x+y <= 32) or ( y <= x+4) or (y>=a)
#
# print(max(a for a in range(0,500) if all(f(x,y,a) for x in range(0,600) for y in range(0,60))))

def f(x,y,a):
    return (2*y + 3*x != 135) or (y > a) or (x > a)

print(max(a for a in range(0,200) if all(f(x,y,a) for x in range(0,400) for y in range(0,400))))