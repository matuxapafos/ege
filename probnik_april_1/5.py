for n in range(10000):
    b = bin(n)[2:]
    s = b.count('1') % 2
    if n % 2 == 0:
        b = '1' + b + str(s)
    if n % 2 != 0:
        b =  b + '0' + str(s)
    if int(b,2) > 100:
        print(n, int(b,2))
