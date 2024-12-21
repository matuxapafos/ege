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
    
    
for n in range(1,1000):
    a = n
    r = ''
    s = 0
    b = (n % 10) * 3
    l = ''
    
    while a !=0:
        re = a%5
        r = str(re) + r
        a //= 5
    
    while b !=0:
        rl = b%5
        l = str(rl) + l
        b //= 5

        
    for i in r:
        s += int(i)
    if s % 2 != 0:
        r = r[-1:]+r[:-1]
  
    if s % 2 == 0:
        r = r+l
        
    if r.count('0') > 2:
        print(n)


    