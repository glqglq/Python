counter = 0
while counter <= 3:
	print 'loop #%d'%(counter)
	counter += 1
	
	
for item in ['e-mail','net-surfing','homework','chat']:
	print item,
print

what = 'Ni!'
who = 'knights'
print 'we are the %s who say %s'%(who,((what+' ')*4))

for eachNum in range(3):
	print eachNum
	
foo = 'abc'
for i in range(len(foo)):
	print foo[i],'(%d)'%i
	
for a,b in enumerate(foo):
	print b,'(%d)'%a
	
squared = [x**2 for x in range(4) if not x %2]
for i in squared:
	print i