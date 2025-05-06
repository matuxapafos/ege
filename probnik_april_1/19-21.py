def f(s,m):
    if 50 <= s <= 119:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s+2,m-1), f(s*3,m-1)]
    return any(h) if m % 2 !=0 else all(h)

print('19)', [s for s in range(1,50) if f(s,2)])
