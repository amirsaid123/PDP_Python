class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = []
        for i in range(len(nums1)):
            for j in range(min(i + 1, len(nums2))):
                if nums1[i] % (nums2[j] * k) == 0:
                    temp = [i, j]
                    result.append(temp)
        return len(result)


nums1 = [1, 3, 4]
nums2 = [1, 3, 4]
result = []
k = 1


for i in range(len(nums1)):
    for j in range(0, i+1):
        if nums1[i] % (nums2[j] * k) == 0:
            temp = [i, j]
            result.append(temp)


print(result)
print(len(result))
