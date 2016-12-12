shares = {}#diction
def Add():
    name = raw_input('Enter the share\'s name:')
    sharet = raw_input('Enter some features of the shares:').split()#list
    share = {}#tuple
    for i in range(len(sharet)):
        Name,Value = sharet[i].split(':')#str
        share.update({Name:Value})#list
    shares[name] = share

def Display():
    while True:
        choice = raw_input('Press 1 for display all,press 2 for display one attribute')
        if choice == '1':
            print shares
        elif choice == '2':
            now = {}
            choice = raw_input('Enter the attribute:')
            for share in shares:
                now.update({share:shares[share][choice]})
            print now
        else:
            print 'Input Wrong!!!'
while True:
    choice = raw_input('Enter your choice:')
    if choice == '1':
        Add()
    elif choice == '2':
        Display()
    else:
        print 'Input Wrong!!!'