x = 2 * 729**333 + 2* 243**334 - 81**335 + 2 *27**336 - 2*9**337 - 338
s = ''
count = 0
while x != 0:
    r = x % 9
    s = str(r) + s
    x //= 9
for i in s:
    if int(i) != '0':
        count += 1
print(count)