class Solution:
    def isValid(self, word: str) -> bool:
        case_1 = False
        case_2 = True
        case_4 = False
        case_5 = False
        if len(word) >= 3:
            case_1 = True
        for letter in word:
            if not letter.isalnum():
                case_2 = False
            if letter.lower() in "auieo":
                case_4 = True
            if letter.lower() in "bcdfghjklmnopqrstvwxyz":
                case_5 = True

        return case_1 and case_2 and case_4 and case_5


obyekt = Solution()
word = input("Enter a word:")
result = obyekt.isValid(word)
print(result)

