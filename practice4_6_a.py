def sum_of_num_over_next(n):
    def loop(n,ans):
        if n >= 1:
            return loop(n-1, ans + n/(n+1))
        else:
            return ans
    return loop(n,0)

print(sum_of_num_over_next(3))