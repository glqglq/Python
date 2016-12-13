def fileIo(path1,path2):
    fin = file(path1,'r')
    fout = file(path2,'w')
    for line in fin:
        line.strip()
        fout.write(line)
    fin.close()
    fout.close()

fileIo('c:\io.txt','c:\io2.txt')