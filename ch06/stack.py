stack = []
def pushIt():
    stack.append(raw_input('Enter new string:').strip())

def popIt():
    if len(stack) == 0:
        print 'cannot pop from an empty stack!'
    else:
        print 'Removed [',repr(stack.pop()),']'

def viewStack():
    print stack

CMDs = {'u':pushIt,'o':popIt,'v':viewStack}

def showMenu():
    pr = """
    p(U)sh
    P(O)p
    (V)iew
    (Q)uit
    Enter choice:"""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print '\nYou picked:[%s]'%choice
            if choice not in 'uovq':
                print 'Invalid option,try again'
            else:
                break
            if choice == 'q':
                break
        CMDs[choice]()

if __name__ == '__main__':
    showMenu()