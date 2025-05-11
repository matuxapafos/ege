alh = '0123456789ABCDEFG'
for x in alh:
    res1 = int('7AC'+x+'53D',17)
    res2 = int('83BG94'+x+'D',17)
    res3 = int('C5'+x+'D',17)
    res4 = int('C4BBF'+x+'4',17)
    res5 = int('7'+x+'79',17)
    if (res1+res2+res3+res4+res5) % 16 == 0:
        print((res1+res2+res3+res4+res5)//16,x)