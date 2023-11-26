def time_passed(fromtime, totime):
    (hour1,_,minute1) = fromtime.partition(":")
    (hour2,_,minute2) = totime.partition(":")
    hour = int(hour2) - int(hour1)
    if minute1 > minute2:

        hour = hour - 1
        minute = 60 - int(minute1) + int(minute2)
    else:
        minute = int(minute2) - int(minute1)
    return str(hour) + ":" + str(minute)

print(time_passed("03:12", "03:25"))
print(time_passed("11:45", "13:15"))
print(time_passed("06:15", "07:45"))
print(time_passed("03:34", "05:00"))