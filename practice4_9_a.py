def even(n):
    if n % 2 == 0:
        return True

def odd(n):
    if n % 2 != 0:
        return True

def sigma2(n):
    if n > 0 and even(n):
        return 2 * sigma2(n / 2) + (n / 2) * (n / 2)
    elif n > 0 and odd(n):
        return n + sigma2(n-1)
    else:
        return 0

print(sigma2(13))