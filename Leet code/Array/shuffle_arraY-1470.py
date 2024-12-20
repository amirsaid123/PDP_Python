class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = nums[:n]
        list2 = nums[n:]
        new_list = []
        for i in range(len(list1)):
            new_list.append(list1[i])
            new_list.append(list2[i])

        return new_list













numbers = [2,5,1,3,4,7]
n = 3

list1 = numbers[:n]
list2 = numbers[n:]
new_list = []

for i in range(n):
    new_list.append(list1[i])
    new_list.append(list2[i])

print(new_list)