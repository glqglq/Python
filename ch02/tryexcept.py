try:
	filename = raw_input("please enter file name")
	fobj = open(filename,'r')
	for eachLine in fobj:
		print eachLine,
	fobj.close()
except IOError,e:
	print 'file open error:',e