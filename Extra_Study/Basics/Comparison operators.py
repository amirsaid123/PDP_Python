# temperature = int(input("Enter the temperature in Celsius: "))
#
# if temperature <= 10 or temperature <= 0:
#     print("It`s a cold day")
# elif temperature <= 30 and temperature >= 10:
#     print("It`s a warm day")
# elif temperature >= 30 and temperature <= 45:
#     print("It`s a hot day")
# elif temperature >= 45:
#     print("It`s an extremely hot day")
#

name = input("Enter your name: ")

if len(name) < 3:
    print("Your name is too short(min:3 characters)")
elif len(name) > 50:
    print("Your name is too long(Max:50 characters)")
else:
    print("Your name is good")