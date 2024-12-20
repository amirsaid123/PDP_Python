class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        yes = []

        for num in arr2:
            if num in arr1:
                while num in arr1:
                    yes.append(num)
                    arr1.remove(num)




        arr1.sort()
        yes.extend(arr1)
        return yes


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * c[num])
            del c[num]
        for k in sorted(c):
            ans.extend([k] * c[k])

        return ans

