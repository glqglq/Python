def fileAccess2(f_str):
    f = open(f_str)
    count = 0
    for line in f:
        print line,
        count += 1
        if count % 5 == 0:
            raw_input('Press any key to continue!')


fileAccess2('c:\io.txt')