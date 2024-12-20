words = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",

}

number = input("Enter a phone number: ")

for num in number:
    print(words.get(int(num)), end=" ")
