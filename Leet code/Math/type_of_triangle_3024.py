class Solution:
    def is_triangel(self, a, b, c) -> bool:
        return a + b > c and a + c > b and c + b > a

    def triangleType(self, nums: List[int]) -> str:
        if not self.is_triangel(nums[0], nums[1], nums[2]):
            return "none"
        else:
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
                return "isosceles"
            else:
                return "scalene"
