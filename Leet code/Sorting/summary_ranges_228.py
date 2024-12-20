class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        if not nums:
            return ranges

        start = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] != 1:
                end = nums[i]
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")

                start = nums[i + 1]


        end = nums[-1]
        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")

        return ranges

