f = open('C:\io.txt','r')
longest = 0
while True:
    linelen = len(f.readline().strip())
    if not linelen:break
    if linelen > longest:
        longest = linelen
f.close()
return longest




#easy way
f = open('C:\io.txt','r')
longest = 0
allLines = f.readlines()
f.close()
for line in allLines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
return longest