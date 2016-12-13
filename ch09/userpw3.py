import time
import pickle
db = {}
def newuser():
    prompt = 'login desired'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken,try another:'
            continue
        else:
            break
    pwd = raw_input('passwd:')
    db[name] = [pwd,time.time()]

def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)[0]
    if passwd == pwd:
        print 'welcome back',name
        if time.time() - db[name][1] <= 14400:
            print 'the time you logined in last time is:',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(db[name][1]))
        db[name][1] = time.time()
    else:
        print 'login incorrect'
def manage():
    cho = raw_input('enter your choice:\n1.delete user.\n2.display all users\n')
    if cho == '1':
        user = raw_input('User:')
        passwd = raw_input('Password:')
        if passwd == db.get(user)[0]:
            print 'User ',user,'has been deleted!'
            del db[user]
    else:
        print db

def showmenu():
    global db
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    (M)anage
    Enter choice"""
    f = open('c:\io.pkl','wb+')
    pickle.dump(db,f,True)
    done = False
    while not done:
        db = pickle.load(f)
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]'%choice
            if choice not in 'neqm':
                print 'invalid option,try again'
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'm':manage()
        if choice == 'e':olduser()
        pickle.dump('c:\io.pkl',True)
if __name__ == '__main__':
    showmenu()