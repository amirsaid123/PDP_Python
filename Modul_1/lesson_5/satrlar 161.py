N = int(input("Enter the number of cards:"))
string = input("Enter the letters:")
letters = string.split()
result = False
if letters.count('A') >= 2 and letters.count('S') >= 2 and 'L' in letters and 'O' in letters and 'M' in letters:
    result = True

print(result)