import types
def displayNumType(num):
    print num,'is a number of type:',
    if type(num) is types.IntType:
        print "a int"
    elif type(num) is types.StringType:
        print 'a str'
    elif type(num) is types.ComplexType:
        print 'a complex'
    elif type(num) is types.FloatType:
        print 'a float'
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(99999999999999)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xss')
