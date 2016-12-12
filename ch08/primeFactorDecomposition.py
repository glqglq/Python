#suyinzifenjie
def getFactors(x):
    return [i for i in range(1,x + 1) if x % i == 0]#list

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            break
        count -= 1
    else:
        return True
    return False

def primeFactorDecomposition(x):
    Factors = getFactors(x)
    now = x
    it = iter(Factors)
    it.next()
    while now != 1:
        i = it.next()
        if now % i == 0:
            now /= i
            it = iter(Factors)
            it.next()
            print i,

primeFactorDecomposition(20)