class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        if len(list1) > len(list2):
            minimum_list = list2
            maximum_list = list1
        else:
            minimum_list = list1
            maximum_list = list2

        dictionary = {}
        for i, word in enumerate(minimum_list):
            if word in maximum_list:
                dictionary[word] = i + maximum_list.index(word)

        common = []
        for key, value in dictionary.items():
            if value == min(dictionary.values()):
                common.append(key)


        return common





