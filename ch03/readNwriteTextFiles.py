'readNwriteTextFile.py--create adn readtext file'

import os
ls = os.linesep

choose = raw_input('please your choose,press 1 to write,press 2 to read:')
if int(choose) == 1:
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
	
if int(choose) == 2:
    fname = raw_input('Enter filename:')
    print

    try:
        fobj = open(fname,'r')
    except IOError,e:
        print '*** file open error:',e
    else:
        for eachLine in fobj:
            print eachLine.strip()
        fobj.close()
else:
#new function