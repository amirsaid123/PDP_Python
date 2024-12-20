class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = 0
        for account in accounts:
            temp = 0
            for value in account:
                temp += value

            if temp > result:
                result = temp

        return result











accounts = [[1, 2, 3], [4,  5, 6]]

result = 0
for account in accounts:
    temp = 0
    for value in account:
        temp += value

        if temp > result:
            result = temp


print(result)