def rot13(x):
    for i in range(len(x)):
        now = ord(x[i]) + 13
        if now > 122:now -= 26#low
        if now > 90 and now < 97:now -= 26#up
        x = x[:i] + chr(now) + x[i + 1:]
    print x

rot13('iloveyou')