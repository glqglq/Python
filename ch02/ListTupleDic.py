aList = [1,2,3,4]
print aList[0]
print aList[2:]
print aList[:3]
aList[1] = 5
print aList

aTuple = ('robots',77,93,'try')
print aTuple
print aTuple[:3]
aTuple[1] = 5


aDict = {'host':'earth'}
aDict['port'] = 80
aDict.keys()
aDict['host']
for key in aDict:
	print key,aDict[key]