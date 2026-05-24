import calendar




c = calendar.Calendar(firstweekday=0)
for day in c.itermonthdays(2026, 5):
    if day != 0:
        print(day)