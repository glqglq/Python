queue = []
def enQ():
    queue.append(raw_input('enter somthing').strip())

def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue'
    else:
        print 'Remove [',repr(queue.pop(0)),']'

def viewQ():
    print queue

cMDs = {'e':enQ,'d':deQ,'v':viewQ}

def showMenu():
    pr = """
    (E)nqueue
    (D)equeue
    (V)iewQueue
    (Q)uit
    Enter choice:"""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print 'You picked:[%s]'%choice
            if choice not in 'devq':
                print 'Invalid option,try again'
            else:
                break
            if choice == 'q':
                break
        cMDs[choice]()

if __name__ == '__main__':
    showMenu()