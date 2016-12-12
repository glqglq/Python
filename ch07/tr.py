def tr(srcstr,dststr,string):
    if len(srcstr) != len(dststr):
        print 'Wrong!'
    Map = zip(list(srcstr),list(dststr))
    Maped = {}
    for i in Map:
        t = tuple(i)
        tt = []
        tt.append(t)
        Maped.update(tt)
    print Maped
    for i in range(len(string)):
        if string[i] in srcstr:
            string = string[:i] + Maped[string[i]] + string[i + 1:]
    print string

tr('abc','mno','abcdef')