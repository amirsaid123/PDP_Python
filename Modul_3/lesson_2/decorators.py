# def my_decorator(func):
#     def wrapper():
#         print("I'm decorating!")
#         func()  # Calling the original function
#     return wrapper
#
#
# @my_decorator  # This is the same as: say_hello = my_decorator(say_hello)
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
#


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("I'm decorating!")
        return func(*args, **kwargs)  # Passing all arguments to the original function
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

