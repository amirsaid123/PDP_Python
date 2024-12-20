class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        result = True
        if len(sentence.split()) == 1:
            return sentence[0] == sentence[-1]

        words = sentence.split()


        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                result = False

            if words[0][0] != words[-1][-1]:
                result = False

        return result


obj = Solution()
print(obj.isCircularSentence("leetcode"))