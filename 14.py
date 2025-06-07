# alp = '0123456789ABCDE'
# for x in alp:
#     res1 = '1'+x+'51'
#     res2 = '3'+x+'2'
#     if (int(res1,15) - int(res2,15)) % 4 == 0:
#         print(x, (int(res1,15) - int(res2,15)) // 4)


# x = 361*2349**84-89**192+1953**481*4843**151
# res = ''
# while x > 0:
#     res += str(x%9)
#     x //= 9
# print(res.count('5'))
# l = []
# for x in '0123456789ABCDEFGHIJ':
#     for y in '0123456789A':
#         for t in '01234567':
#             res1 = int('1'+x+y,20)
#             res2 = int('3' + y,11)
#             res3 = int('4'+y,11)
#             res4 = int(t+'1',8)
#             if (res3 - res4) != 0:
#                 res = (res1 + res2)//(res3 - res4)
#                 if res % 5 == 0:
#                     l.append(res)
# print(max(l))

# x = 5 ** 2 * 7 ** 25 + 6 ** 2*7**36-4**2*9**3
# res = ''
# while x > 0:
#     res += str(x%7)
#     x //= 7
# print(res.count('0'))

# for x in '0123456789ABCDEFGHIJKLMNOPQRS':
#     res = int('47'+x+'42696', 29) + int('8'+x+'22', 29)
#     if res % 28 == 0:
#         print(x,res//28)

# x = 2*729**333+2*243**334-81**335+2*27**336-2*9**337-338
# res = ''
# while x>0:
#     res += str(x%9)
#     x //= 9
# print(len(res) - res.count('0'))

# for x in '0123456789ABCDEFGHI':
#     res = int('98897'+x+'21',19) + int('2' + x + '923',19)
#
#     if res % 18 == 0:
#         print(x,res // 18)

# count = 0
# l = []
# alp = {11,12,13,14,15,16,17}
# count = 0
# for x in '0123456789A':
#     for y in 'BCDEFGH':
#         for z in alp:
#             res = int('5'+x+y+'A',18) + int('18' + x + '7', int(z))
#             count += 1
# print(count)


for x in '0123456789ABCDEFGHIJKLMNOPQ':
    res = int('17'+x+'35',27) + int(x+'742M',27) + int(x,27)**3

    if res % 23 == 0:
        print(x,res//23)
