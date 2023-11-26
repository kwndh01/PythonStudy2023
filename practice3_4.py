def median(x,y,z):
    smallest = x
    if y < smallest:
        smallest = y
    if z < smallest:
        smallest = z

    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z

    if x != largest and x != smallest:
        return x
    elif y != largest and y != smallest:
        return y
    else:
        return z

print(median(1,3,5))
print(median(3,5,1))
print(median(3,3,3))
print(median(3,5,3))
print(median(3,5,5))
