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

s = open('0wGUBUjFW.txt').readline()

while '++' in s: s = s.replace('++', '+ +')
while '+*' in s: s = s.replace('+*', '+ *')
while '*+' in s: s = s.replace('*+', '* +')
while '**' in s: s = s.replace('**', '* *')
mx = float('-inf')
for kusok in s.split():
    mx = max(mx,len(kusok))
print(mx)


