class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        result =[]

        items1 = dict(items1)
        items2 = dict(items2)

        if len(items1) > len(items2):
            for key, val in items1.items():
                if key in items2.keys():
                    summa = val + items2[key]
                    temp = [key, summa]
                    result.append(temp)
                else:
                    temp = [key, val]
                    result.append(temp)

            for key, val in items2.items():
                if key not in items1.keys():
                    temp = [key, val]
                    result.append(temp)
        else:
            for key, val in items2.items():
                if key in items1.keys():
                    summa = val + items1[key]
                    temp = [key, summa]
                    result.append(temp)
                else:
                    temp = [key, val]
                    result.append(temp)

            for key, val in items1.items():
                if key not in items2.keys():
                    temp = [key, val]
                    result.append(temp)



        result.sort(key=lambda x: x[0])


        return result


# class Solution:
#     def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
#         result = []
#         if len(items1) > len(items2):
#             max_list = items1
#             min_list = items2
#         else:
#             max_list = items2
#             min_list = items1
#
#         min_list = dict(min_list)
#         max_list = dict(max_list)
#
#         for key, val in max_list.items():
#             if key in min_list.keys():
#                 summa = val + min_list[key]
#                 temp = [key, summa]
#                 result.append(temp)
#             else:
#                 temp = [key, val]
#                 result.append(temp)
#
#         for key, value in min_list.items():
#             if key not in max_list.items():
#                 temp = [key, value]
#                 result.append(temp)
#
#         result.sort(key=lambda x: x[0])
#
#         return result

