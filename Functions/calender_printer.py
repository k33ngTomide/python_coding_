import calendar


def print_calendar(date: str):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    cal = calendar.TextCalendar()

    cal_str = cal.formatmonth(year, month)

    print(cal_str)

    day_of_week = calendar.day_name[calendar.weekday(year, month, day)]
    print(f"The specified date ({year}-{month:02d}-{day:02d}) is a {day_of_week}")


print_calendar("2023-09-15")
