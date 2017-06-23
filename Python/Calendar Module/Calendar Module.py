import calendar

day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
m, d, y = map(int, raw_input().split())
date = calendar.weekday(day=d, month=m, year=y)
print day_of_week[date].upper()

