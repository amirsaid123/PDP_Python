class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            counter = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            result.append(counter)

        return result





nums = [8,1,2,2,3]
result = []

for i in range(len(nums)):
    counter = 0
    for j in range(0,len(nums)):
        if nums[i]>nums[j]:
            counter += 1
    result.append(counter)



print(result)
