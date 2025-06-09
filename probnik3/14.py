for x in '0123456789ABCDE':
    res = int('1' + x+ '51',15) - int('3' + x + '2',15)
    if res % 4 == 0:
        print(x, res//4)