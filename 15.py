# def f(x):
#     return (x & 57 == 0) or ((x & 23 == 0) <= (not(x & a == 0)))


# for a in range(1,1000):
#     if all(f(x) for x in range(1,100000)):
#         print(a)
#         break

# def deli(x,y):
#     return x % y == 0
#
# for a in range(1,10000):
#     if all((not(deli(x,7) and deli(x,13)) <= (x > a -40)) for x in range(1,10000)):
#         print(a)

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

# def f(x,y,a):
#     return (2*y + 3*x != 135) or (y > a) or (x > a)
#
# print(max(a for a in range(0,200) if all(f(x,y,a) for x in range(0,400) for y in range(0,400))))


# def f(x):
#     p = 17 <= x <= 65
#     q = 29<= x <= 75
#     a = a1 <= x <= a2
#     return
#
# r = []
# d = [y for x in (17,29,58,80) for y in (x, x-0.1,x+0.1)]
#
# for a1 in d:
#     for a2 in d:
#         if all(f(x) == 1 for x in d) and a2 >= a1:
#             r += [a2-a1]
# print(round(min(r)))

# def d(n,m):
#     return n % m == 0
#
# for a in range(1,200):
#     if all((d(x,3) <= (not (d(x,2)))) or (x-a >= 4) for x in range(1,400)):
#         print(a)

# for x in range(-500,100):
#      p = x in [2,4,6,8,10,12,14,16,18,20]
#      q = x in [5,10,15,20,25,30,25,40,45,50]
#      a = 1
#      f_usl = 1
#      f = (a <= p) and (q <= (not a))
#      if f == f_usl:
#          print(x)


# def f(x):
#     p = 13<= x <= 19
#     q = 17 <= x <= 23
#     a = a1 <= x <= a2
#     return (not(not(p)<= q) <= q) <= (a <= ((not q) <= p))
# r = []
# d = [y for x in (13,17,19,23) for y in (x,x-0.1,x+0.1)]
# for a1 in d:
#     for a2 in d:
#         if all(f(x) == 1 for x in d) and a2 >= a1:
#             r += [a2-a1]
# print(round(max(r)))


# def f(x):
#     p = 12 <= x <= 28
#     q = 15 <= x <= 30
#     a = a1 <= x <= a2
#     return ((p) <= (a)) and (((not(q)) or (a)))
#
# r = []
# d = [y for x in (12,15,28,30) for y in (x,x-0.1,x+0.1)]
#
# for a1 in d:
#     for a2 in d:
#         if all(f(x) == 1 for x in d) and a2 >= a1:
#             r += [a2-a1]
# print(round(min(r)))

# def d(n,m):
#     return n % m == 0
#
# for a in range(1,200):
#     if all((d(x,2) <= (not(d(x,3)))) or ((x + a >= 100)) for x in range(1,400)):
#         print(a)


# def f(x,y,a):
#     return (x + 2 * y != 58) or ((a - x>0) == (a + y > 0))
#
# print(min(a for a in range(1,200) if all(f(x,y,a) for x in range(1,400) for y in range(1,400))))


# def p(n,m):
#     if n - m >= 0:
#         return 1
#     else:
#         return 0
# for a in range(0,200):
#     if all((not (p(x +y, 73 ))) or (not ( p(37,x-y) )) or p(y,a) for x in range(0,400) for y in range(0,400)):
#         print(a)

def d(n,m):
     return n % m == 0

def sumb(s,d):
    return s + d > 0

for a in range(1,200):
    if all( (x + a >= 160) or d(x,7) <= (not(sumb(x,-17))) for x in range(1,400)):
        print(a)