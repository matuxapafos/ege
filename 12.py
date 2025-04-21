# x = 200* "*"

# count = 0
# while "****" in x or "???" in x:
#     if '****' in x:
#         x = x.replace("****", "???", 1)
#         count+=3
#     x = x.replace("??", "*", 1)

    
# print(count)
# m = float('+inf')
# for n in range(11,2000):
#     x = '3' + '5'*n
#     res = 0
#     while '25' in x or '355' in x or '555' in x:
#         if '25' in x:
#            x = x.replace('25','32',1)
#         if '355' in x:
#             x = x.replace('355','25',1)
#         if '555' in x:
#             x = x.replace('555','3',1)
#     for i in x:
#         res += int(i)
#     if res %25 == 0:
#         print(n)
#         break

# for n in range(4, 10000):
#     s = '5' + '2'*n
#     while '52' in s or '2222' in s or '1122' in s:
#         if '52' in s:
#             s = s.replace('52', '11')
#         if '2222' in s:
#             s = s.replace('2222', '5')
#         if '1122' in s:
#             s = s.replace('1122', '25')
#     if sum(map(int,s)) == 64:
#         print(n)
n = float('-inf')
for m in range(4,10000):
    res = 0
    s = '1' + '2'*m
    while '12' in s or '322' in s or '222' in s:
        if '12' in s: s = s.replace('12','2',1)
        if '322' in s: s = s.replace('322','21',1)
        if '222' in s: s = s.replace('222', '3', 1)
    n = max(n,sum(map(int,s)))
print(n)
