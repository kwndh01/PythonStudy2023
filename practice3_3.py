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
def frontOK(s):
    if len(s) >= 7:
        inputYear = int(s[0]) * 10 + int(s[1])
        if int(s[0]) != 0 and int(s[0]) != 1 and int(s[0]) != 2:
            old = True
            year = '19' + str(inputYear)
            year = int(year)
        else:
            old = False
            year = '20' + str(inputYear)
            year = int(year)
        month = int(s[2]) * 10 + int(s[3])
        day = int(s[4]) * 10 + int(s[5])
        verify = is_valid_date(year, month, day)

        if 1 == int(s[6]) or 2 == int(s[6]) or 5 == int(s[6]) or 6 == int(s[6]):
            if old == False:
                checkPoint1 = True
            else:
                checkPoint1 = False
        elif 3 == int(s[6]) or 4 == int(s[6]) or 7 == int(s[6]) or 8 == int(s[6]):
            if old == True:
                checkPoint1 = True
            else:
                checkPoint1 = False
        else:
            checkPoint1 = False

        if checkPoint1 == True and verify == True:
            return True
        else:
            return False
    else:
        return False



def backOK(s):
    (front, mid, back) = s.partition("-")
    s = front + back
    verify = 11 - ((2 * int(s[0]) + 3 * int(s[1]) + 4 * int(s[2]) + 5 * int(s[3]) + 6 * int(s[4]) + 7 * int(s[5]) + 8 * int(s[6]) + 9 * int(s[7]) + 2 * int(s[8]) + 3 * int(s[9]) + 4 * int(s[10]) + 5 * int(s[11])) % 11)

    if verify == 10:
        if int(s[12]) == 0:
            return True
        else:
            return False
    elif verify == 11:
        if int(s[12]) == 1:
            return True
        else:
            return False
    else:
        return False

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return frontOK(front+back[0]) and mid == "-" and backOK(s)

print(isRRN(str(120813-4111111)))