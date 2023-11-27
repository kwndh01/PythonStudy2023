def add_range(start, end, step):
    ans = 0
    while end > start:
        ans = ans + start
        start = start + step
    return ans

print(add_range(1,10,1))
print(add_range(1,10,2))
print(add_range(1,10,3))
print(add_range(-5,6,2))
