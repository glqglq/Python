import random

choice = {'jianzi':0,'shitou':1,'bu':2}

user = raw_input('Enter user''s choice:')
com = random.randint(0,2)
if (com > choice[user]) or (com == 'jianzi' and user == 'bu'):
    print 'computer wins!'
else:
    print 'user wins!'