# f = open("assert_and_raise.py", "r")
# print(f.read())
# f.close()



# while True:
#     num1, num2 = map(int, input("Enter two numbers: ").split())
#     with open("numbers", 'a') as file:
#         file.write(f"{num1} + {num2} = {num1 + num2}\n")
#


# n = int(input("Enter a number: "))
# for i in range(n+1):
#     with open("numbers", "a") as f:
#         f.write(str(i) + " ")
#

with open("numbers", 'w') as f:
    nums:list = f.readlines()
    for num in nums:
        if int(num) % 2 != 0:
            nums.remove(num)

