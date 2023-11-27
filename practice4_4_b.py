def square(n):
    n = abs(n)
    ans = 1
    while n > 1:
        ans = ans + (2 * n - 1)
        n = n - 1
    return ans

print(square(0))
print(square(1))
print(square(-2))
print(square(3))
print(square(-4))
print(square(5))
