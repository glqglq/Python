#Example:123.456.789.159   123456789
def intToIp(x):
    x = str(x)
    if len(x) == 12:
        x = x[0:3] + ':' + x[3:6] + ':' + x[6:9] + ':' + x[9:12]
        return x
    else:
        print 'length wrong!'

def ipToInt(x):
    x = x[0:3] + x[4:7] + x[8:11] + x[12:15]
    return int(x)


#if __name__ == '__mian__':
print intToIp(123456789159)
print ipToInt('123.456.789.159')