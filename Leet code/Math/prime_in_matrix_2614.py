class Solution:
    def is_prime(self, n: int) -> bool:
        for i in range(2, n**0.5 + 1):
            if n % i == 0:
                return False
        return True


    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diagonals = []


        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j == len(nums[i]) - 1 or i == j:
                    if self.is_prime(nums[i][j]):
                        diagonals.append(nums[i][j])

        return max(diagonals)


