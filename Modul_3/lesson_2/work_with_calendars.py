import calendar
#
# yy = 2024
# mm = 10
# print(calendar.month(yy, mm))
#


# import calendar
# print ("The calendar of year 2024 is : ")
# print (calendar.calendar(2024))


# first_weekday, num_days = calendar.monthrange(2024, 10)
# print(f"First weekday: {first_weekday}, Total days: {num_days}")

#
# calendar.setfirstweekday(calendar.SUNDAY)
#
#
# print(calendar.month(2024, 10))

# weeks = calendar.monthcalendar(2024, 10)
# for week in weeks:
#     print(week)

# def find_fridays(year, month):
#     fridays = []
#     for week in calendar.monthcalendar(year, month):
#         if week[calendar.FRIDAY] != 0:
#             fridays.append(week[calendar.FRIDAY])
#     return fridays
#
# print("Fridays in October 2024:", find_fridays(2024, 10))


# cal = calendar.TextCalendar()
#
# for day in cal.iterweekdays():
#     print(day)

