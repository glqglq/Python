before = raw_input('Enter names and nums:').split()#list
after = {}
for i in range(len(before)):
    before[i] = before[i].split(':')
    before[i][1] = int(before[i][1])
    #after.update(tuple(before[i]))
after.update(tuple(before))
sortedafter = sorted(after)
for i in sortedafter:
    print i,':',after[i],' ',
"""
for i in range(len(after)):
    after[i][0],after[i][1] = after[i][1],after[i][0]
sortedafter = sorted(after)
for i in sortedafter:
    print after[i],':',i,' ',
"""