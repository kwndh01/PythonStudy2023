def monthly_payment_plan(principle, interest, year):
    r = interest / 12 / 100
    m = year * 12
    return ((1 + r) ** m * principle * r) / ((1 + r) ** m - 1)

print(monthly_payment_plan(10000000, 2.8, 4))