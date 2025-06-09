s = '4'*30 + '53' * 30
while '43' in s or '53' in s:
    if '43' in s: s = s.replace('43', '33')
    else: s = s.replace('53','433')
print(s.count('3'))