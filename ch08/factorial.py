def factorial(x):
    sum = 1
    for i in range(1,x + 1):
        sum *= i
    return sum

print factorial(4)