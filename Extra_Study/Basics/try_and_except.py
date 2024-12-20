# try:
#     age = int(input("Enter your age:"))
#     print("Your age is", age)
# except ValueError:
#     print("Invalid input")
#
class NegativeNumberError(Exception):
    """Exception raised for errors in the input if the number is negative."""
    def __init__(self, value):
        self.value = value
        self.message = f"Negative number error: {value} is not allowed."
        super().__init__(self.message)

def process_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 2

try:
    num = int(input("Enter a non-negative number: "))
    result = process_number(num)
    print(f"The square of the number is: {result}")
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer.")
