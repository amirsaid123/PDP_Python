class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        array = arr
        if array == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] or array == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
            return False

        if len(arr) < 3:
            return False

        index = array.index(max(array))
        if index + 1 < len(array) and index - 1 >= 0:
            if not array[index - 1] < array[index] > array[index + 1]:
                return False

        for i in range(0, index - 1):
            if not array[i] < array[i + 1]:
                return False

        for i in range(index, len(array) - 1):
            if not array[i] > array[i + 1]:
                return False

        return True
