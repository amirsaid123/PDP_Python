class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = []
        sorted_scores = sorted(score, reverse=True)
        rank_map = {}

        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_map[s] = "Gold Medal"
            elif i == 1:
                rank_map[s] = "Silver Medal"
            elif i == 2:
                rank_map[s] = "Bronze Medal"
            else:
                rank_map[s] = str(i + 1)

        for num in score:
            result.append(rank_map[num])

        return result



# score = [10, 3, 8, 9, 4]
# result = []
#
# sorted_scores = sorted(score, reverse=True)
#
#
# rank_map = {}
#
#
# for i, s in enumerate(sorted_scores):
#     if i == 0:
#         rank_map[s] = "Gold Medal"
#     elif i == 1:
#         rank_map[s] = "Silver Medal"
#     elif i == 2:
#         rank_map[s] = "Bronze Medal"
#     else:
#         rank_map[s] = str(i + 1)
#
#
# for num in score:
#     result.append(rank_map[num])
#
# print(result)
