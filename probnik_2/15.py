def f(x,y,a):
    return (x*y < a) or (x < y) or (9<x)

print(min(a for a in range(0,200) if all(f(x,y,a) for x in range(0,400) for y in range(0,400))))