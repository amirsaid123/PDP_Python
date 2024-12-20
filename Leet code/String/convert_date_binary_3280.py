class Solution:
    def convertDateToBinary(self, date: str) -> str:
        data = date.split('-')
        result = []
        for dat in data:
            temp = bin(int(dat))[2:]
            result.append(temp)

        result = "-".join(result)
        return result






obj = Solution()
print(obj.convertDateToBinary("2080-02-29"))
