def f(x,y):
    if x > y:
        return 0
    if x ==y:
        return 1
    else:
         return f(x+3,y) + f(x+4,y) + f(x+2,y)
print(f(6,32) * f(32,35) * f(35,44))