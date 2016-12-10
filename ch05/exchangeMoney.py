def exchangeMoney(x):
    x = x * 100
    twentyfive = x // 25
    x = x % 25
    ten = x // 10
    x = x % 10
    five = x //5
    x = x % 5
    return {'twentyfive':twentyfive,'ten':ten,'five':five,'one':x}

total = exchangeMoney(0.76)
print 'twentyfive:%d'%total['twentyfive']
print 'ten:%d'%total['ten']
print 'five:%d'%total['five']
print 'one:%d'%total['one']