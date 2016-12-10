str = list(raw_input('Enter a string:'))
str2 = ''
for i in range(len(str)):
    if str[i].isupper() :
        str2 += str[i].lower()
    elif str[i].islower():
        str2 += str[i].upper()
    else:
        str2 += str[i]
print str2