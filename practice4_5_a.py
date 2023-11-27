def permutation(n,k):
    def loop(n,k,ans):
        if k > 0:
            return loop(n-1, k-1, ans * n)
        else:
            return ans
    return loop(n,k,1)

print(permutation(4,3))