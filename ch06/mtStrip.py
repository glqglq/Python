myString = raw_input('enter a string')
for i in range(len(myString)):
    if myString[i] != ' ':
        Front = i
        break
for i in range(len(myString) - 1,-1,-1):
    if myString[i] != ' ':
        Bottom = i
        break
print '-',myString[Front:Bottom + 1],'-'