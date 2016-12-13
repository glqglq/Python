def countLine(f_str):
    f = open(f_str,'r')
    count = 0
    for line in f:
        count += 1
    return count

print countLine('c:\io.txt')