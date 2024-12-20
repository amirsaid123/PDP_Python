# def plus_one(number):
#     return number + 1
#
# add_one = plus_one
# print(add_one(5))
#



# def plus_one(number): #1
#     def add_number(number): #3
#         return number + 1 #5
#
#     result = add_number(number) #4
#     return result #6
#
#
# print(plus_one(5)) #2, #7


# def plus_one(number): #1
#     return number + 1 #6
#
# def function_call(function): #2
#     number_to_add = 5 #4
#     return function(number_to_add) #5, #7
#
#
# print(function_call(plus_one)) #3, #8


# def hello_function(): #1
#     def say_hi(): #3
#         return "Hello World!" #7
#     return say_hi #4
#
# hello = hello_function() #2, #5
# print(hello()) #6, #8


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def say_hi():
    return "hello there"

decorate = uppercase_decorator(say_hi)
print(decorate())


