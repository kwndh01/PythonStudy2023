def addtime(time1, time2):
    h1, m1, s1 = map(int, time1.split(":"))
    h2, m2, s2 = map(int, time2.split(":"))

    total_seconds = s1 + s2
    seconds = total_seconds % 60
    total_minutes = m1 + m2 + total_seconds // 60
    minutes = total_minutes % 60
    hours = h1 + h2 + total_minutes // 60

    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

print(addtime("0:14:57", "0:25:02"))
