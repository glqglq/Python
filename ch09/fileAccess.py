def fileAccess(n,f_str):
    f = open(f_str,'r')
    now = 0
    for line in f:
        now += 1
        if now > n:
            break
        print line,


fileAccess(3,'c:\io.txt')