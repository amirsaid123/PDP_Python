class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        for letter in s:
            if letter.isdigit():
                nums.append(int(letter))

        if len(nums) == 0:
            return -1

        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) > 1:
            return nums[-2]
        else:
            return -1
