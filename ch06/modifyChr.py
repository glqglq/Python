#KMP?
def findchr(string,char):
    for i in range(len(string) - len(char) + 1):
        flag = 1
        ii = i
        for j in range(len(char)):
            if string[ii] != char[j]:
                flag = 0
                break
            ii += 1
        if flag == 1:
            return i


def rfindchr(string,char):
    for i in range(len(string) - 1,len(char) - 2,-1):
        flag = 1
        ii = i
        for j in range(len(char) - 1,-1,-1):
            if string[ii] != char[j]:
                flag = 0
                break
            ii -= 1
        if flag == 1:
            return i - len(char) + 1
print findchr('hehadmin','admin')
print rfindchr('hehadminadmin','admin')