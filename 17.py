# numbers = [int(x) for x in open('17.txt')]
# mn = min(x for x in numbers if 100<= x <= 999 and x % 10 == 3)
# ans = []
# for i in range(len(numbers) -1):
#     if (1000<= numbers[i] <= 9999) + (1000<= numbers[i+1] <= 9999) == 1 :
#         if (numbers[i] ** 2 + numbers[i+1] ** 2) % mn == 0 :
#             ans.append(numbers[i] ** 2 + numbers[i+1] ** 2)
# print(len(ans), max(ans))


# numbers = [int(x) for x in open('17.txt')]
# mn = min(numbers)
# count = 0
# mx = float('-inf')
# for i in range(len(numbers) -1 ):
#     if numbers[i] % 117 == mn or numbers[i+1] % 117 ==mn:
#         mx = max(mx, numbers[i]+numbers[i+1])
#         count += 1
#
# print(count, mx)

# numbers = [int(x) for x in open('17.txt')]
# mx = max(x for x in numbers if 10<= x <= 99)
# ans = []
# for i in range(len(numbers) - 1):
#     if (10<= numbers[i] <= 99) + (10<= numbers[i+1] <= 99) == 1:
#         if (numbers[i] + numbers[i+1]) % mx == 0:
#             ans.append(numbers[i] + numbers[i+1])
# print(len(ans), max(ans))

# num = [int(x) for x in open('17.txt')]
# mn = min(abs(x) for x in num)
#
# ans =[]
# for i in range(len(num) - 1):
#     if (num[i] < 0) + (num[i+1] <0) == 1:
#         if ((num[i] + num[i+1]) > 0) and ((num[i] + num[i+1]) % mn == 0):
#             ans.append(num[i] + num[i+1])
# print(len(ans), max(ans))

# num = [int(x) for x in open('17.txt')]
# mn = max(x for x in num if 100<=x<=999)
# ans = []
# for i in range(len(num) -1):
#     if (100<=abs(num[i]) <= 999) + (100<= abs(num[i+1]) <= 999) == 1:
#         if (num[i] + num[i+1]) <= mn:
#             ans.append(num[i] + num[i+1])
# print(len(ans), max(ans))

# def p(x):
#     return x > 1 and all(x% d != 0 for d in range(2,int((x**0.5))+1))
#
# num = [int(x) for x in open('17.txt')]
# ans = []
# for i in range(len(num) -2 ):
#     u1 = str(num[i]).count('3') > 0
#     u2 = str(num[i+1]).count('3') > 0
#     u3 = str(num[i+2]).count('3') > 0
#     if u1 and u2 and u3:
#         if p(num[i] + num[i+1] + num[i+2]) == 1:
#             ans += [num[i] + num[i+1] + num[i+2]]
#
# print(len(ans), min(ans))
# def p(x):
#     return x > 1 and all(x%d != 0 for d in range(2,int((x**0.5)) + 1))
#
#
# num = [int(x) for x in open('UZY_Q-7K9.txt')]
# mn = max(x for x in num if abs(x)%100 == 17)
# ans =[]
# for i in range(len(num) -1):
#     if p(num[i]) + p(num[i+1]) == 1:
#         if (num[i] + num[i+1]) % mn == 0:
#             ans += [num[i] * num[i+1]]
# print(len(ans), max(ans))

# num = [int(x) for x in open('17.txt')]
# mx = max(abs(x) for x in num if x % 1001 == 0)
#
# ans = []
# for i in range(len(num) -1):
#     if (100<= abs(num[i]) <= 999) or (100<= abs(num[i+1])<= 999):
#         if (num[i] + num[i+1]) > mx:
#             ans += [num[i] + num[i+1]]
# print(len(ans), min(ans))


num = [int(x) for x in open('17.txt')]
mx = max(x for x in num if abs(x) % 100 == 54)
count = 0
mnp = float('-inf')
for i in range(len(num)- 1):
    if abs(num[i]) % 10 == abs(num[i+1]) % 10:
        if abs(num[i]) + abs(num[i+1]) <= mx:
            count += 1
            maxi = max(num[i], num[i+1])
            mnp = max(mnp,maxi)


print(count,mnp)



