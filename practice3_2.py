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
def is_valid_date(year,month,day):
    if year > 0:
        leapYear = isLeapyear(year)
        if 12 > month > 0:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 0 < day <= 31:
                    return True
                else:
                    return False
            else:
                if month == 2:
                    if leapYear == True:
                        if 0 < day <= 29:
                            return True
                        else:
                            return False
                    else:
                        if 0 < day <= 28:
                            return True
                        else:
                            return False
                else:
                    if 0 < day <= 28:
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False

print(is_valid_date(2019,11,31)) #False


