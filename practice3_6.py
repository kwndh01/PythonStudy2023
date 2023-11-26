from math import sqrt

def quadratic_equation_positive(a, b, c):
    if a != 0:
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            return x1, x2
        else:
            return None
    else:
        return None

print(quadratic_equation_positive(1, -1, -2))
print(quadratic_equation_positive(3, 3, 3))
print(quadratic_equation_positive(0, 3, 4))
