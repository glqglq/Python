'makeTextFile.py--create text file'

import os
ls = os.linesep

#get filename
while True:
    fname = raw_input('input filename')
    if os.path.exists(fname):#pan duan lu jing shi fou you xiao
	    print "ERROR:'%s' already exists" % fname
    else:
		break

#get file content (text) lines
all = []
print "\nEnter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s'%(x,ls) for x in all])
fobj.close()
print 'DONE'