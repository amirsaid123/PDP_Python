def alarm_clock(day, vacation):
    if (day > 0 and day < 6) and not vacation:
        return "7:00"
    elif (day == 0 or day == 6) and not vacation:
        return "10:00"
    elif (day > 0 and day < 6) and vacation:
        return "10:00"
    elif (day == 0 or day == 6) and vacation:
        return "off"


print(alarm_clock(0, False))