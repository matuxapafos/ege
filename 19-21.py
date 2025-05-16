# 1 кучка
#
# def f(s, m):
#     if s >= 61:  # условие победы
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(s + 3, m - 1), f(s + 10, m - 1), f(s * 2, m - 1)]  # все возможые ходы
#     return any(h) if m % 2 != 0 else all(h)  # если первый ход проигрышный, то меняем all на any
#
#
# print("19)", [s for s in range(1, 61) if f(s, 1)])  # допустимые значения и на каком ходу закончится игра
# print("20)", [s for s in range(1, 61) if not f(s, 1) and f(s, 2)])
# print("21)", [s for s in range(1, 61) if not f(s, 1) and f(s, 3)])

# 2 кучи
# def f(a,b,m):
#     if a+b >= 143:
#         return m % 2 ==0
#     if m == 0:
#         return 0
#     h = [f(a+3,b,m-1), f(a,b+3,m-1), f(a*2,b,m-1), f(a,b*2,m-1)]
#     return any(h) if m % 2 !=0 else all(h)
#
# print([s for s in range(1,124) if f(16,s,2)])

# def f(a,b,m):
#     if a == b:
#         return m % 2 ==0
#     if m == 0:
#         return 0
#     if a < b:
#         h = [f(a+1,b,m-1), f(a+3,b,m-1)]
#         return any(h) if m % 2 != 0 else all(h)
#     if a > b:
#         h =[ f(a, b + 1, m - 1), f(a, b + 3, m - 1)]
#         return any(h) if m % 2 != 0 else all(h)
#
# print([s for s in range(1,24) if (not f(13,s,1)) and f(13,s,2)])


# def f(s,m):
#     if s <=1:
#         return m%2 ==0
#     if m == 0:
#         return 0
#     if s >= 4:
#         h = [f(s-1,m-1), f(s-4,m-1)]
#         return any(h) if m % 2 != 0 else any(h)
#     if s % 3 == 0:
#         h = [f(s-1,m-1), f(s//3,m-1)]
#         return any(h) if m %2 !=0 else any(h)
#
# print([s for s in range(4,101) if not f(s,1) and f(s,2)])


# def f(s,m):
#     if s >= 39:
#         return m%2==0
#     if m ==0:
#         return 0
#
#     h = [f(s+1,m-1), f(s+3,m-1),f(s*2,m-1)]
#     return any(h) if m%2!=0 else all(h)
#
# print('19)', [s for s in range(1,39) if not f(s,1) and f(s,2)])
# print('20)', [s for s in range(1,39) if not f(s,1) and f(s,3)])
# print('21)', [s for s in range(1,39) if not f(s,2) and f(s,4)])


def f(a,b,m):
    if a + b >= 123: 
        return m % 2 ==0
    if m == 0: 
        return 0

    h = [f(a+1,b,m-1), f(a*2 ,b,m-1), f(a,b+1,m-1), f(a,b*2,m-1)]
    return any(h) if m % 2 != 0 else all(h)


print('19)', [s for s in range(1,110) if f(13,s,2)])
print('20)', [s for s in range(1,110) if not f(13,s,1) and f(13,s,3)])
print('21)', [s for s in range(1,110) if not f(13,s,2) and f(13,s,4)])
