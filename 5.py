# list = []

# for n in range(1,1000):
#     r = bin(n)[2:]
#     if r.count('1') % 2 == 0:
#         r = r + '0'
#     if r.count('1') % 2 != 0:
#         r = r + '1'
#     if r.count('1') % 2 == 0:
#         r = r + '0'
#     if r.count('1') % 2 != 0:
#         r = r + '1'
        
#     if int(r,2) < 86:
#         list.append(n)
        
# print(max(list))        
    
    
# for n in range(1,1000):
#     a = n
#     r = ''
#     s = 0
#     b = (n % 10) * 3
#     l = ''
    
#     while a !=0:
#         re = a%5
#         r = str(re) + r
#         a //= 5
    
#     while b !=0:
#         rl = b%5
#         l = str(rl) + l
#         b //= 5

        
#     for i in r:
#         s += int(i)
#     if s % 2 != 0:
#         r = r[-1:]+r[:-1]
  
#     if s % 2 == 0:
#         r = r+l
        
#     if r.count('0') > 2:
#         print(n)

for n in range(1000,10000):
    sumc = 0
    maxn = float('-inf')
    minn = float('+inf')
    for i in str(n):
        maxn = max(int(i), maxn)
        minn = min(int(i), minn)
        if int(i) % 2 ==0:
            sumc += int(i)
    d = sumc**2
    c = maxn-minn
    e = c ** 3
    if d > e:
        res = str(e) + str(d)
    else:
        res = str(d) + str(e)
    if res == '4343':
        print(n)

    