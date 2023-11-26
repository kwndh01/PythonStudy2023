def even(x):
    return x % 2 == 0
def smaller_odd(x,y):
    if even(x) == True:
        if even(y) == True:
            return None
        else:
            return y
    else:
        if even(y) == True:
            return x
        else:
            if x < y:
                return x
            else:
                return y

def smallest_odd(x,y,z):
    if x == smaller_odd(x,y):
        return smaller_odd(x,z)
    elif y == smaller_odd(x,y):
        return smaller_odd(y,z)

print(smallest_odd(3,2,2))
print(smallest_odd(3,5,7))