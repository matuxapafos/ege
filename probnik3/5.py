for n in range(1,1000):
    b = bin(n)[2:]
    if n % 5 == 0:
        b = b + b[-3:]
    if n % 5 != 0:
        a = (n%5) * 59
        
        b = b + bin(a)[2:]
    if int(b,2) > 256:
        print(n)