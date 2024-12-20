class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = ""
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) <= 2:
                words[i] = words[i].lower()
            else:
                words[i] = words[i].lower().capitalize()

        result = " ".join(words)
        return result



print(Solution().capitalizeTitle("capiTalIze tHe titLe"))
