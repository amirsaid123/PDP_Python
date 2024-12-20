string = input("Enter a string:")

for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        print(string[i], end=" ")
        



