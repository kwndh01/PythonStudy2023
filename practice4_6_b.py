def sum_of_num_over_next(n):
    ans = 0
    while n >= 1:
        ans = ans + n / (n + 1)
        n = n - 1
    return ans

print(sum_of_num_over_next(3))