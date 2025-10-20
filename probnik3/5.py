a = int(input().strip())
b = []
for _ in range(a):
    b.append(input().strip())

c = int(input().strip())
d = []
for _ in range(c):
    d.append(input().strip())

e = {}
for f, g in enumerate(b, 1):
    # Разбиваем строку на слова и проверяем каждое слово
    h = g.split()
    for i in h:
        # Убираем ВСЕ знаки препинания из слова
        j = ''.join(char for char in i if char.isalpha())
        if j and j[0].isupper():
            if j not in e:
                e[j] = f

for k in d:
    print(e.get(k, -1))