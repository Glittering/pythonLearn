import math

def quadratic_equation(a, b, c):
    if b * b - 4 * a * c >= 0:
        x1 = (-b + math.sqrt(b*b-4*a*c)) / 2 * a
        x2 = (-b - math.sqrt(b*b-4*a*c)) / 2 * a
    else:
        x1 = x2 = null
    return x1, x2

print quadratic_equation(2.0, 3.0, 0)
print quadratic_equation(1.0, -6.0, 5)
