import os
have = []
donothave = []
def documentString(p_str):
    global have
    global donothave
    p_str += '\\'
    files = os.listdir(p_str)
    for f in files:
        if os.path.isfile(p_str+f) and f[-1] == 'y' and f[-2] == 'p' and f[-3] == '.':
            ff = open(p_str+f,'r')
            flag = 0
            for line in ff:
                if '__doc__' in line:
                    flag = 1
            if flag == 1:
                have += [f]
            else:
                donothave += [f]

documentString('C:\Python27\Lib')
print 'have:',have
print 'donot have:',donothave