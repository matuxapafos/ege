for n in range(1,1000):
    r = ''
    b = bin(n)[2:]
    if n % 3 == 0:
        for i in b:
            if i == '0':
                r += '11'
            else: r += '1'
    if n % 3 != 0:
        for i in b:
            if i == '1':
                r += '10'
            else: r+='0'
    if int(r,2) <= 161:
        print(int(r,2))