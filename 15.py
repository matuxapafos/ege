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
