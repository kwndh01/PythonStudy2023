def shift(ds, move):
    if move < 0:
        length = len(ds)
        output = ds[:length + move]
    else:
        output = ds + '0' * move

    return output

print(shift("11011", 3))
print(shift("11011", 2))
print(shift("11011", 1))
print(shift("11011", 0))
print(shift("11011", -1))
