# s = open('24.txt').readline()
#
# while 'ad' in s: s = s.replace('ad', 'a d')
# while 'da' in s: s = s.replace('da', 'd a')
#
# l = []
# for kusok in s.split(' '):
#     for i in range(len(kusok) - 1):
#         ps = kusok[i]
#         for j in range(i + 1, len(kusok)):
#             ps += kusok[j]
#         l.append(len(ps))
# print(max(l))

# s = open('HIJpUMRws.txt').readline()
#
# while 'AA' in s: s = s.replace('AA', 'A A')
# while 'BB' in s: s = s.replace('BB', 'B B')
# while 'CC' in s: s = s.replace('CC', 'C C')
# while 'AB' in s: s = s.replace('AB', 'A B')
# while 'AC' in s: s = s.replace('AC', 'A C')
# while 'BA' in s: s = s.replace('BA', 'B A')
# while 'CA' in s: s = s.replace('CA', 'C A')
# while 'BC' in s: s = s.replace('BC', 'B C')
# while 'CB' in s: s = s.replace('CB', 'C B')
# while '88' in s: s = s.replace('88', '8 8')
# while '89' in s: s = s.replace('89', '8 9')
# while '99' in s: s = s.replace('99', '9 9')
# while '98' in s: s = s.replace('98', '9 8')
# l = []
# for kusok in s.split():
#     for i in range(len(kusok) -1):
#         ps = kusok[i]
#         for j in range(i+1,len(kusok)):
#             ps += kusok[j]
#         l.append(len(ps))
# print(max(l))

# s = open('24.txt').readline()
#
# while 'AB' in s: s = s.replace('AB','A B')
#
# s = s.split()
# print(max(sum(len(kusok) for kusok in s[i: i+51]) for i in range(len(s) -50)))

# s = open('XBGwzXHsB.txt').readline()
# while 'OO' in s: s = s.replace('OO', 'O O')
# while 'OP' in s: s = s.replace('OP', 'O P')
# while 'ON' in s: s = s.replace('ON', 'O N')
# while 'PP' in s: s = s.replace('PP', 'P P')
# while 'PO' in s: s = s.replace('PO', 'P O')
# while 'PN' in s: s = s.replace('PN', 'P N')
# while 'NN' in s: s = s.replace('NN', 'N N')
# while 'NO' in s: s = s.replace('NO', 'N O')
# while 'NP' in s: s = s.replace('NP', 'N P')
# l =[]
# for kusok in s.split():
#     l.append(len(kusok))
# print(max(l))

# s = open('IGVcRTjyP.txt').readline()
# while '**' in s: s = s.replace('**', '* *')
# while '*+' in s: s = s.replace('*+', '* +')
# while '+*' in s: s = s.replace('+*', '+ *')
# while '++' in s: s = s.replace('++', '+ +')
# m = float('-inf')
# for kusok in s.split():
#     if len(kusok) > m:
#         for i in range(len(kusok)- 1):
#             ps = kusok[i]
#             if ps[0] not in '*+' and kusok[i] + kusok[i+1] not in ['00','01','02', '03', '04', '05', '06', '07', '08', '09']:
#                 for j in range(i+1, len(kusok)):
#                     ps += kusok[j]
#                     if ps[-1] not in '*+':
#                         if eval(ps) == 0:
#                             m = max(m, len(ps))
# print(m)

# s = open('bI4DufyyF.txt').readline()
#
# while '--' in s: s = s.replace('--', '- -')
# while '-*' in s: s = s.replace('-*', '- *')
# while '*-' in s: s = s.replace('*-', '* -')
# while '**' in s: s = s.replace('**', '* *')
# ans = []
# for kusok in s.split():
#     for i in range(len(kusok) -1):
#         ps = kusok[i]
#         if ps[0] not in '0-*':
#             for j in range(i+1, len(kusok)):
#                 ps += kusok[j]
#                 if ps[-1] not in '*-' and '-0' not in ps and '*0' not in ps:
#                     ans.append(len(ps))
# print(max(ans))

# s = open('0wGUBUjFW.txt').readline()
#
# while '++' in s: s = s.replace('++', '+ +')
# while '+*' in s: s = s.replace('+*', '+ *')
# while '*+' in s: s = s.replace('*+', '* +')
# while '**' in s: s = s.replace('**', '* *')
# mx = float('-inf')
# for kusok in s.split():
#     mx = max(mx,len(kusok))
# print(mx)

# s = open('kC3I96Zwxx.txt').readline()
#
# while '--' in s: s = s.replace('--', '- -')
# while '-*' in s: s = s.replace('-*', '- *')
# while '*-' in s: s = s.replace('*-', '* -')
# while '**' in s: s = s.replace('**', '* *')
# ans = []
# for kusok in s.split():
#     for i in range(len(kusok)-1):
#         ps = kusok[i]
#         if ps[0] == 'B' and kusok[i] + kusok[i+1] not in ['B-', 'B*']:
#             for j in range(i+1,len(kusok)):
#
#                 ps += kusok[j]
#                 if ps[-1] not in '*-' and 'A' not in ps and 'C' not in ps and 'D' not in ps and ps.count('B') == 1:
#                     ans.append(len(ps))
# print(max(ans))

# s = open('24.txt').readline()
# mx = -float('inf')
# s = s.replace('B','f').replace('D', 'f').replace('C','f').replace('A','a').replace('O','a')
# count = 0
# for i in range(0, len(s)-1, 2):
#     if s[i] == 'f' and s[i+1] == 'a':
#         count += 1
#         mx = max(mx, count)
#     else:
#         count = 0
# print(mx)

# s = open('24.txt').readline()
# while 'QW' in s: s = s.replace('QW', 'Q W')
#
# answer = []
#
# for kusok in s.split():
#     answer += [len(kusok)]
# print(max(answer))

# s = open('24.txt').readline()
# while 'XX' in s: s =s.replace('XX', 'X X')
# while 'YY' in s: s =s.replace('YY', 'Y Y')
# while 'ZZ' in s: s =s.replace('ZZ', 'Z Z')
# ans = []
# for kusok in s.split():
#     ans += [len(kusok)]
# print(max(ans))

# s = open('24.txt').readline()
# s =s.replace('1','n').replace('2','c').replace('3','n').replace('4','c').replace('5','n').replace('6','c').replace('7','n').replace('8','c').replace('9','n').replace('0','c')
#
# while 'nc' in s: s = s.replace('nc', 'n c')
# while 'cn' in s: s = s.replace('cn', 'c n')
#
# ans = []
# for kusok in s.split():
#     ans += [len(kusok)]
# print(max(ans))

# s = open('24.txt').readline()
#
# while 'PR' in s: s = s.replace('PR','P R')
# while 'RP' in s: s = s.replace('RP','R P')
# ans = []
# for kusok in s.split():
#     ans += [len(kusok)]
# print(max(ans))


# s = open('24.txt').readline()
# while 'XX' in s: s = s.replace('XX', 'X X')
# while 'YY' in s: s = s.replace('YY', 'Y Y')
# ans = []
# for kusok in s.split():
#     for i in range(len(kusok) -1):
#         ps = kusok[i]
#         for j in range(i+1,len(kusok)):
#             ps += kusok[j]
#             if ps.count('X') == 1 and ps.count('Y') == 1:
#                 ans.append(len(ps))
# print(max(ans))

s = open('24.txt').readline()
mx = float('-inf')
count = 0
for i in range(0,len(s) -2,3):
    if (s[i] == 'N' and s[i+1] == 'P' and s[i+2] =='O') or (s[i] == 'P' and s[i+1] == 'N' and s[i+2] =='O'):
        count += 1
        mx = max(mx,count)
    else:
        count = 0
print(mx)
