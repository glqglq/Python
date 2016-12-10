class FooClass(object):
	version = 0.1
	name = 'me'
	def _init_(self,nm = 'John Doe'):
		self.name = nm
		print 'Create a class instance for',nm
	def showname(self):
		print 'Your name is',self.name
		print 'My name is',self.__class__.__name__
	def showver(self):
		print self.version
	def addMe2Me(self,x):
		return x+x

fool = FooClass()
fool.showname()
fool.showver()
print fool.addMe2Me('xyz')