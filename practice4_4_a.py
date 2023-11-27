def square(n):
    n = abs(n)
    def loop(n, ans):
        if n > 1:
            return loop(n - 1, ans + (n * 2 -1))
        else:
            return ans
    return loop(n, 1)

print(square(0))
print(square(1))
print(square(-2))
print(square(3))
print(square(-4))
print(square(5))
