# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         words = sentence.split(' ')
#         n = len(searchWord)
#         find_word = ""
#         index = -1
#         for word in words:
#             if word[:n] == searchWord:
#                 find_word = word
#                 index = words.index(find_word) + 1
#                 break
#         return index
#
#
#
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word[:len(searchWord)] == searchWord:
                return i+1
        return -1










obyekt = Solution()
sentence = input("Enter a sentence:")
searchWord = input("Enter a searchWord:")
result = obyekt.isPrefixOfWord(sentence, searchWord)
print(result)
