def fac(n):
    def loop(n, ans):
        if n > 1:
            return loop(n-1, ans + n)
        else:
            return ans + 1
    return loop(n,0)

print(fac(10))