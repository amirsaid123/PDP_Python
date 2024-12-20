from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        evens = [i for i in nums if i % 2 == 0]
        if len(evens) == 0:
            return -1
        counter = Counter(evens)
        maximum = max(counter.values())
        candidates = [num for num, freq in counter.items() if freq == maximum]
        minimum = min(candidates)
        return minimum






# nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
# evens = [i for i in nums if i % 2 == 0]
# if len(evens) == 0:
#     print(-1)
# counter = Counter(evens)
# maximum = max(counter.values())
# candidates = [num for num, freq in counter.items() if freq == maximum]
# print(min(candidates))
# print(counter)
# print(counter.most_common(1)[0][0])
