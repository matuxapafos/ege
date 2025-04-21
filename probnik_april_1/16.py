
def f(n):
    if  n <3 : return n + 1
    if n % 2 ==0: return f(n-2) + n - 2
    if n % 2 != 0: return f(n+2) + n + 2
c = 0
for i in range(1, 10000):
    try:
        if 9999<f(i) <= 99999:
            c += 1
    except:
        ...
print(c)