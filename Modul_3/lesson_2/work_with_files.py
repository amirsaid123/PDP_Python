import calendar
def to_print(file:bool):
    def inner(function):
        def wrapper(*args, **kwargs):
            if file:
                result = function(*args, **kwargs)
                with open("calendar.txt", "a") as f:
                    f.write(f"{result}\n")
            else:
                return function(*args, **kwargs)
        return wrapper
    return inner



@to_print(file=True)
def create_calendar(*args):
    if len(args) == 1:
        return calendar.calendar(*args)
    if len(args) == 2:
        return calendar.month(*args)


print(create_calendar(2024, 10))