"""
myStr = raw_input('please enter a string')
for i in range(0,len(myStr),1):
    print myStr[i],
print

for i in range(len(myStr) - 1,-1,-1):
    print myStr[i],
print
"""

"""
myStr1 = raw_input('Input the first string')
myStr2 = raw_input('Input the second string')
if len(myStr1) != len(myStr2):
    print 'not equal'
else:
    flag = 0
    for i in range(len(myStr1)):
        if myStr1[i] != myStr2[i]:
            flag = 1
            print 'not equal'
            break
    if flag == 0:
        print 'equal'
"""

reverseString = list(raw_input('entet a String'))
reverseString += list(reverseString).reverse()
print reserveString