def count_vowels (word: str):
    counter_vowels = 0
    counter_consonants = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            counter_vowels += 1
        else:
            counter_consonants += 1

    return counter_vowels, counter_consonants



word = input("Enter a word:")
print(count_vowels(word))

