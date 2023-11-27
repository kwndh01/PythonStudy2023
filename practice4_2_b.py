def fac(n):
    ans = 1
    while n > 1:
        n , ans = n-1, ans + n
    return ans

print(fac(10))