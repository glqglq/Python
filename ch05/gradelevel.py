def gradelevel(x):
    if x >= 90 and x <= 100:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

print gradelevel(66)