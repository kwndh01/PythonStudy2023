def minutes_after(time, minuteplus):
    (hour, _, minute) = time.partition(":")
    hourplus = minuteplus // 60
    minuteplus = minuteplus % 60
    minute = int(minute) + minuteplus
    minute_to_hour = minute // 60
    minute = str(minute % 60)
    hour = str(int(hour) + hourplus + minute_to_hour)
    return hour + ":" + minute

print(minutes_after("3:34", 100))
print(minutes_after("11:45", 20))
print(minutes_after("9:59", 1))
print(minutes_after("123:10", 200))