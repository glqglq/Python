import math
def sSquare(x):
    return x ** 2

def vCube(x):
    return x ** 3

def sCircle(r):
    return (r ** 2) * math.pi

def vBall(r):
    return 4.0/3*math.pi*(r ** 3)

print sSquare(3)
print vCube(3)
print sCircle(3)
print vBall(3)