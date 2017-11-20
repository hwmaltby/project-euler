#Henry Maltby 2017

def days_in_month(month, year):
    longest = [1, 3, 5, 7, 8, 10, 12]
    middle = [4, 6, 9, 11]
    if month in longest:
        return 31
    if month in middle:
        return 30
    year = year % 400
    if year % 4 == 0 and (year % 100 != 0 or year == 0):
        return 29
    return 28

def counting_sundays(start, end, day):
    day %= 7
    month = 1
    count = 1 if (day == 0) else 0
    while start != end:
        day += days_in_month(month, start)
        day %= 7
        if day == 0:
            count += 1
        if month == 12:
            start += 1
            month = 0
        month += 1
    return count

print(counting_sundays(1901, 2001, 1 + 365))