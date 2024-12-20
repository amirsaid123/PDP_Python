class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1


        max_length = max(max_length, current_length)

        return max_length


nums = [1,3,5,7]
result = []

if nums[0] <= nums[1]:
    result.append(nums[0])

for i in range(1, len(nums)-1):
    if nums[i] <= nums[i+1] and nums[i] >= nums[i-1]:
        result.append(nums[i])
    else:
        if nums[i] > nums[i-1]:
            result.append(nums[i])

if nums[-1] == max(nums):
    result.append(max(nums))

print(result)