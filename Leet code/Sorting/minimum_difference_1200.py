class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        differences = []
        for i in range(len(arr) - 1):
            differences.append(arr[i + 1] - arr[i])

        min_difference = min(differences)

        result = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_difference:
                temp = [arr[i], arr[i + 1]]
                result.append(temp)
        return result



# arr = [4, 2, 1, 3]
# arr.sort()
# differences = []
# for i in range(len(arr)-1):
#     differences.append(arr[i+1]-arr[i])
#
# min_difference = min(differences)
#
# result = []
# for i in range(len(arr)-1):
#     if arr[i+1] - arr[i] == min_difference:
#         temp = [arr[i], arr[i+1]]
#         result.append(temp)
#
# print(result)
