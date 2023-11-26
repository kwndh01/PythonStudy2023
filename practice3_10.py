def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    hour = int(hour)
    if 0<= hour <= 11 or hour == 24:
        minute = minute + 'am'
        if hour == 0 or hour == 24:
            hour = 12
        else:
            pass
    else:
        minute = minute + 'pm'
        if hour != 12:
            hour = hour - 12
    hour = str(hour)
    return hour +':' + minute

print(clock24to12("00:00"))
print(clock24to12("00:05"))
print(clock24to12("09:58"))
print(clock24to12("11:43"))
print(clock24to12("12:08"))
print(clock24to12("15:50"))
print(clock24to12("20:20"))
print(clock24to12("24:00"))