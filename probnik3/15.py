def f(x):
    p = 5 <= x <= 280
    q = 295 <= x <= 400
    r = 375 <= x <= 450
    a = a1 <= x <= a2
    return ((q) <= (p)) or ((not(a)) <= (r))
ans = []
d = [y for x in (5,280,295,375,400,450) for y in (x, x - 0.1, x+0.1)]
for a1 in d:
    for a2 in d:
       if all(f(x) == 1 for x in d) and a2>= a1:
           ans += [a2-a1]
print(round(min(ans)))