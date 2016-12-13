def textProcessing(f_str):
    f = open(f_str,'r')
    text = f.readlines()
    text2 = []
    for i in range(len(text)):
        if len(text[i]) > 8:
            t = text[i][8:]
            t2 = text[i][:8] + '\n'
            text2 += [t2] + [t]
        else:
            text2 += text[i]
            #print text[i],
    f2 = open(f_str,'w')
    for i in range(len(text2)):
        f2.write(text2[i])

textProcessing('c:\io.txt')