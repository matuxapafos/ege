c = 0
for line in open('9_2.txt'):
    a = [int(x)for x in line.split()]
    pov = [s for s in a if a.count(s) == 2]
    nepov = [s for s in a if a.count(s) == 1]
    if len(pov) == 4 and len(nepov) == 3:
        if sum(pov)/len(pov) < sum(a)/7:
            c += 1

print(c)