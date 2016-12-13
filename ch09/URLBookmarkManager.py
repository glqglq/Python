path = 'c:\bookMark.txt'
def addURLBookMark():#add
    global path
    bookMark = raw_input('Enter the bookmark(name url description) you want to add:')
    f = open(path,'a')
    f.write(bookMark + os.linesep)

def modifyURLBookMark():
    modifyByName = raw_input('Enter the name you want to modify:')
    f = open(path,'w')
    for line in f:
        if modifyByName == line.split()[0]:
            newBookMark = raw_input('Enter new attribute:')
            
	else:
        print 'No Such Bookmark!'