string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

minimum = min(string1, string2, key=len)
maximum = max(string1, string2, key=len)

longest_substring = ""


for i in range(len(minimum)):
    for j in range(i + 1, len(minimum) + 1):
        substring = minimum[i:j]
        if substring in maximum and len(substring) > len(longest_substring):
            longest_substring = substring

print("Longest common substring:", longest_substring)
