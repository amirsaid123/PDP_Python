class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        summa = sum(apple)
        capacity.sort(reverse=True)
        counter = 0
        i = 0
        while counter < summa:
            counter += capacity[i]
            i += 1

        return i
