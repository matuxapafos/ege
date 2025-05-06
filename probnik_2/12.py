s = '112'*4 + 4*'1'
su =0
while '11' in s:
    if '112' in s: s = s.replace('112', '7', 1)
    else: s = s.replace('11','3', 1)

for i in s:
    su += int(i)

print(su)
