def fileFilter(x):
    f = open(x,'r')
    for line in f:
        line = line.strip()
        if line[0] != '#':
            print line

fileFilter('c:\io.txt')