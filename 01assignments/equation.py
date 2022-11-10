from math import sqrt


def computerequation(a, b, c):
    x = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    return x

print(computerequation(22, 66, 9))


