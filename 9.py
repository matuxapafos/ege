# from math import prod
# count = 0
# for lines in open("9.txt"):
#     a = [int(x) for x in lines.split()]
#     pov = [x for x in a if a.count(x) >1]
#     ne_pov = [x for x in a if a.count(x)== 1]
#     if len(pov) > 0:
#         if 3*sum(ne_pov) <= prod(pov):
#             count += 1
            
# print(count)
# k = 0
# for line in open('9.txt'):
#     k += 1
#     a = [int(x) for x in line.split()]
#     pov = [x for x in a if a.count(x) > 1]
#     y = [x for x in pov if sum(int(x)) % 2 == 0]
    
#     if a == sorted(a):
#         if len(y) > 0:
#             print(k)
# from math import *
# count = 0
# for line in open("9.txt"):
#     a = [int(x) for x in line.split()]
#     otr = [x for x in a if x<0]
#     pol = [x for x in a if x>0]
#     pov = [x for x in a if a.count(x)==2]
#     ne_pov = [x for x in a if a.count(x) == 1]
#     if len(pov) == 2 and len(ne_pov) == 4:
#         if abs(sum(otr)) > sum(pol):
#             count += 1
            
# print(count)

# count = 0

# for line in open('9.txt'):
#     a = [int(x) for x in line.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     ne_pov = [x for x in a if a.count(x) == 1]
    
#     if len(pov) == 3 and len(ne_pov) == 3:
#         if (sum(pov) ** 2) > (sum(ne_pov) ** 2):
#             count += 1
            
# print(count)
    
    