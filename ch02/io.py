import sys
name = "gongluqi"
age = 21
print "i am %s,my age is %d"%(name,age)


print>>sys.stderr,'Fatal error:invalid input'

logfile = open('C:\io.txt','a')
print>>logfile,'\nhahahaa'
logfile.close()

user = raw_input('enter a number:\n')
print int(user)