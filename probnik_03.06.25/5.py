for n in range(1,10000):
    b = oct(n)[2:]
    maxn = float('-inf')
    minn = float('+inf')
    for i in str(b):
        maxn = max(maxn,int(i))
        minn = min(minn,int(i))
    e = minn*2
    d = oct(e)[2:]
    if n % 2 ==0:
        b = str(b)+str(maxn)
    if n % 2 !=0:
        b = str(b)+str(d)
    if int(b,8)< 313:
        print(n)
