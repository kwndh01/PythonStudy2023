def validclock24(time):
    (hour,colon,minute) = time.partition(":")
    if len(hour) == 2:
        hour = int(hour)
        if 0 <= hour <= 23:
            pass
        else:
            return False
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

print(validclock24("00:00"))
print(validclock24("00:30"))
print(validclock24("09:58"))
print(validclock24("12:15"))
print(validclock24("23:59"))
print(validclock24("24:00"))
print(validclock24("7:07"))
print(validclock24("07:121"))
print(validclock24("13:4"))
print(validclock24("00:60"))
print(validclock24("24:01"))
print(validclock24("25:10"))
