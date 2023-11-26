def smaller(x,y):
    if x < y:
        return x
    else:
        return y

def smallest(x,y,z):
    return smaller(smaller(x,y),z)
def median(x,y,z):
    if x == smallest(x,y,z):
        return smaller(y,z)
    elif y == smallest(x,y,z):
        return smaller(x,z)
    else:
        return smaller(x,y)


print(median(1,3,5))
print(median(3,5,1))
print(median(3,3,3))
print(median(3,5,3))
print(median(3,5,5))
