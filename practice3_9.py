def validclock12(time):
    (hour,colon,minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]

    hour = int(hour)
    if 0 < hour <= 12:
        pass
    else:
        return False

    if len(minute) == 2:
        minute = int(minute)
        if 0 <= minute <= 59:
            return True
        else:
            return False
    else:
        return False

print(validclock12("1:30am"))
