# x = int(input("Enter a number: "))
# assert x < 0, "Number should  be negative"
# print(x)


try:
    x = int(input("Enter a number: "))
    assert x < 0, "Number should not be positive"
    print(x)
except AssertionError as error:
    print(f"AssertionError: {error}")
