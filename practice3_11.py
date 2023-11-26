def clock12to24(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]

    hour = int(hour)
    if hour == 12 and am_or_pm == 'am':
        hour = '00'
    else:
        if am_or_pm == 'pm':
            if hour != 12:
                hour = hour + 12
                hour = str(hour)
            else:
                hour = str(hour)
        else:
            hour = '0' + str(hour)

    return hour + ':' + minute

print(clock12to24('12:00am'))
print(clock12to24('12:05am'))
print(clock12to24('1:30am'))
print(clock12to24('3:05am'))
print(clock12to24('12:00pm'))
print(clock12to24('12:08pm'))
print(clock12to24('3:50pm'))
print(clock12to24('9:12pm'))
print(clock12to24('11:59pm'))