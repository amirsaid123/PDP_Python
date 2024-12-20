class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = ""
        for i in num:
            number += str(i)

        number = int(number)
        number += k

        my_num = [int(i) for i in str(number)]
        return my_num


