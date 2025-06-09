count = 0
for lines in open('9.txt'):
    a = [int(x) for x in lines.split()]
    pv = [x for x in a if a.count(x) >= 2]
    nec = [x for x in a if x % 2 !=0]
    usl1 = len(pv) >= 2
    usl2 = len(nec) == 3
    if usl1 + usl2 == 1:
        count += 1
print(count)
