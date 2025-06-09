def p(x):
    return x > 1 and all(x % d != 0 for d in range(2,int(x**0.5) + 1))

ans = []

numbers = [int(x) for x in open('17.txt')]
for i in range(len(numbers) -2):
    if (str(numbers[i]).count('3') >= 1) and (str(numbers[i+1]).count('3') >= 1) and (str(numbers[i+2]).count('3') >= 1):
        if p(numbers[i] + numbers[i+1] + numbers[i+2]):
            ans.append(numbers[i] + numbers[i+1] + numbers[i+2])
print(len(ans), min(ans))
