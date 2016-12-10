def exchangeTime(t):
    t = t.split(':')
    return int(t[0]) * 60 + int(t[1])


print exchangeTime('22:30')