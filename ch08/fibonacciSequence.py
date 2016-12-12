s = [1,1]
def fibonacciSequence(x):
    for i in range(2,x):
        global s
        s += [s[i - 1] + s[i - 2]]
    return s[x - 1]

print fibonacciSequence(7)