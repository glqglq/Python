import random
before1 = set()
before2 = set()
i = 0
while i < 10:
    before1.add(random.randint(0,9))
    i += 1
i = 0
while i < 10:
    before2.add(random.randint(0,9))
    i += 1
print 'A|B:',before1|before2,'A&B:',before1&before2