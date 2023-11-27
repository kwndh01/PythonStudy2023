def add_range(start, stop, step):
    def loop(start, stop, step, ans):
        if stop > start:
            return loop(start + step, stop, step, ans + start)

        else:
            return ans
    return loop(start, stop, step, 0)

print(add_range(1,10,1))
print(add_range(1,10,2))
print(add_range(1,10,3))
print(add_range(-5,6,2))
