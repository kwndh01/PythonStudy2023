def isLeapyear(year):
    if year >= 0:
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return None

print(isLeapyear(0))
print(isLeapyear(1))
print(isLeapyear(4))
print(isLeapyear(2010))
print(isLeapyear(2011))
print(isLeapyear(2012))
print(isLeapyear(2013))
print(isLeapyear(2016))
print(isLeapyear(1900))
print(isLeapyear(2000))
print(isLeapyear(2020))
print(isLeapyear(2100))
print(isLeapyear(2200))
print(isLeapyear(2400))
print(isLeapyear(-2000))
