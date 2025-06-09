f = open('24.txt').readline()
f = f.replace('1','n').replace('3','n').replace('5','n').replace('7','n').replace('9','n')
count = 0
mx = float('-inf')
for i in range(len(f) -2):
    if (str(f[i]) + str(f[i+1]) + str(f[i+2])) != 'nnn':
        count += 1
        mx = max(mx,count)
    else:
        count = 0

print(mx+2)