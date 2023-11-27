def isleapyear(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def next_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if isleapyear(year):
            return 29
        else:
            return 28


def date_after_n_days(year, month, day, n):
    day += n
    while day > days_in_month(year, month):
        day -= days_in_month(year, month)
        year, month = next_month(year, month)
    return year, month, day

print(date_after_n_days(2019,4,20,2))
print(date_after_n_days(2019,4,20,7))
print(date_after_n_days(2019,4,20,10))
print(date_after_n_days(2019,4,20,11))
print(date_after_n_days(2019,4,20,50))
print(date_after_n_days(2019,4,20,100))
print(date_after_n_days(2019,4,20,200))
print(date_after_n_days(2019,4,20,300))
print(date_after_n_days(2019,4,20,1000))