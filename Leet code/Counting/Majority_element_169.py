class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        major_element = 0
        for num in nums:
            if nums.count(num) > n / 2:
                major_element = num
                break
        return major_element





