def caculator(x):
    x = x.split()
    if x[1] == '+':
        return int(x[0]) + int(x[2])
    elif x[1] == '-':
        return int(x[0]) - int(x[2])
    elif x[1] == '*':
        return int(x[0]) * int(x[2])
    elif x[1] == '/':
        return int(x[0]) / int(x[2])
    elif x[1] == '%':
        return int(x[0]) % int(x[2])
    elif x[1] == '**':
        return int(x[0]) ** int(x[2])

print caculator('1 + 2')
print caculator('2 - 2')
print caculator('1 / 2')
print caculator('1 * 2')
print caculator('1 % 2')
print caculator('1 ** 2')