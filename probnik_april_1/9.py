count = 0
for line in open('99.txt'):
    a = [int(x) for x in line.split()]
    pov = [x for x in a if a.count(x) == 2]
    nepov = [x for x in a if a.count(x) == 1]
    if len(pov) == 4 and len(nepov) == 1:
        if pov[0] < nepov[0] < pov[2] or pov[3] < nepov[0] < pov[1]:
            count += 1
print(count)