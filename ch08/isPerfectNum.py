def getFactors(x):
    return [i for i in range(1,x) if x % i == 0]#list

def isPerfectNum(x):
    if sum(getFactors(x)) == x:
        print "Yes!"
    else:
        print "NO!"

isPerfectNum(8128)