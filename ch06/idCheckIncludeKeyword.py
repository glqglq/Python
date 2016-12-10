import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0\nTestees must be at least 2 chars long.'
myInput  = raw_input('Identifier to test?')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid:first symbol must be alphabetic.'''
    else:
        if myInput in keyword.kwlist:
            print 'key word!'
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print '''invalid:remaining symbols must be alphanumeric'''
                    break
            else:
                print 'ok'