from itertools import count, accumulate, chain, compress, dropwhile, filterfalse, groupby, islice, pairwise, starmap, \
    product
from itertools import tee, zip_longest, permutations

# def my_cycle(iterable):
#     while True:
#         for item in iterable:
#             yield item
#
#
#
# for i in my_cycle([1, 2, 3, 4, 5]):
#     print(i)


# for i in count(10):
#     print(i)


# def my_count(start, step = 1):
#     while True:
#         yield start
#         start += step
#
#
# for i in my_count(10, 4):
#     print(i)

# for i in accumulate([1, 2, 3, 4, 5, 6, 7, 8]):
#     print(i)
#
# print()
#
# def my_accumulate(iterable):
#     total = 0
#     for value in iterable:
#         total += value
#         yield total
#
#
#
#
# for i in my_accumulate([1, 2, 3, 4, 5, 6, 7, 8]):
#     print(i)



# def my_repeat(item, step):
#     i = 1
#     while i <= step:
#         yield item
#         i += 1
#
#
# for i in my_repeat(10, 3):
#     print(i)



# def my_batch(iterable, n):
#     for i in range(0, len(iterable), n):
#         yield iterable[i:i + n]
#
#
#
# for i in my_batch("ABCDEFGHJHSJBJD", 6):
#     print(i)


# def my_chain(*iterables):
#     for i in iterables:
#         for j in i:
#             yield j
#
# for i in my_chain(["ABC", "DEF"], "amirsaid", (1, 2, 3)):
#     print(i)


# my_list = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
#
# joined_list = chain.from_iterable(my_list)
#
# for i in joined_list:
#     print(i)


# def join_lists(iterable):
#     result = []
#     for list in iterable:
#         for item in list:
#             result.append(item)
#     return result
#
#
#
# for i in join_lists([[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]):
#     print(i)


# my_list = [1, 2, 3, 4, 5]
# selectors = [1, 0, 1, 0, 1]
#
# for i in compress(my_list, selectors):
#     print(i)


# def my_compress(data: list, selectors:list) -> list:
#     result = []
#     for i in range(len(selectors)):
#         index = i
#         if selectors[i] == 1:
#             result.append(data[index])
#
#     return result
#
#
# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# selectors = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#
# for item in my_compress(my_list, selectors):
#     print(item)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in dropwhile(lambda x: x < 5, my_list):
#     print(i)


# def my_drop(function, iterable):
#     dropping = True
#     for item in iterable:
#         if dropping:
#             if not function(item):
#                 dropping = False
#                 yield item
#         else:
#             yield item
#
#
# for i in my_drop(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
#     print(i)



# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = filterfalse(lambda x: x % 2 == 0, my_list)
#
# for i in result:
#     print(i)


# def my_filter(function, iterable):
#     for item in iterable:
#         if not function(item):
#             yield item
#
#
#
#
# for i in my_filter(lambda x: x % 2 == 0, my_list):
#     print(i)


# my_list = ["A", "B", "DEF"]
#
# result = groupby(my_list, key=len)
#
# for i, item in result:
#     print(i, list(item))




# data = [('Dog', 'Mammal'), ('Cat', 'Mammal'), ('Goldfish', 'Fish'), ('Parrot', 'Bird'), ('Labrador', 'Mammal')]
#
#
# grouped = groupby(data, key=lambda x: x[1])
#
# for key, group in grouped:
#     print(key, list(group))


# def group(iterable, key):
#     for item in iterable:
#         if key(item):
#             yield key(item), item
#
#
# grouped = group(data, key=lambda x: x[0])
#
# for key, group in grouped:
#     print(key, list(group))


# my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',]

# group = islice(my_letters, 3, len(my_letters), 3)
#
# for letter in group:
#     print(letter)
#


# def my_slice(iterable, stop, start = 0,  step=1):
#     result = []
#     for i in range(start, stop, step):
#         result.append(iterable[i])
#
#     return result
#
#
#
#
# for i in my_slice(my_letters, 4):
#     print(i)
#




# for letter in pairwise(my_letters):
#     print(letter)

#
# def to_pair(iterable):
#     for i in range(len(iterable)-1):
#         yield iterable[i], iterable[i+1]
#
#
#
# for letter in to_pair(my_letters):
#     print(letter)


# def add(*args):
#     return sum(args)
#
#
# data = [(1, 2, 3,), (4, 5, 6), (7, 8, 9)]
#
# result = starmap(add, data)
#
# for item in result:
#     print(item)


# def my_starmap(function, iterable):
#     for args in iterable:
#         yield function(*args)
#
#
#
#
# def add(*args):
#     return sum(args)
#
#
# my_numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
#
# result = my_starmap(add, my_numbers)
#
# for i in result:
#     print(i)
#


# def my_takewhile(function, iterable):
#     result = []
#     for item in iterable:
#         if function(item):
#             result.append(item)
#
#     return result
#
#
#
# my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# result = my_takewhile(lambda x: x < 5, my_number)
#
# for res in result:
#     print(res)


my_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# iter1, iter2, iter3 = tee(my_number, 3)
#
# for item in iter1:
#     print(item)
#
# print()
# for item in iter2:
#     print(item)


# def my_tee(iterable, n=2):
#     iterators = [[] for _ in range(n)]
#     for item in iterable:
#         for i in range(n):
#             iterators[i].append(item)
#     return (iter(iterators[i]) for i in range(n))
#
#
# my_letters = ['a', 'b', 'c', 'd', 'e']
#
#
# iter1, iter2 = my_tee(my_letters)
#
#
# print("Iterator 1:")
# for item in iter1:
#     print(item)
#
#
# print("Iterator 2:")
# for item in iter2:
#     print(item)


# list_1 = ['a', 'b', 'c', 'd']
# list_2 = [1, 2, 3]
# list_3 = ["hi", "hello", "hullo"]
#
# result = zip_longest(list_1, list_2, list_3, fillvalue="/")
#
# for i in result:
#     print(i)


# list_1 = ['a', 'b', 'c', 'd']
# list_2 = [1, 2, 3]
# list_3 = ["hi", "hello", "hullo"]


# result = product(list_1, list_2, list_3, repeat=10000)
#
# for res in result:
#     print(res)


# def my_product(*args, value=1):
#     result = [[]]
#
#     for arg in args:
#         result = [x + [y] for x in result for y in arg]
#
#     for item in result:
#         yield tuple(item)
#
#
# list_1 = ['a', 'b', 'c', 'd']
# list_2 = ['1', '2', '3']
# list_3 = ["hi", "hello", "hullo"]
#
# result = my_product(list_1, list_2, list_3)
#
# for result in result:
#     print(result)




# data = [1, 2, 3]
# perm = permutations(data)
#
#
# for p in perm:
#     print(p)



# def my_permutations(iterable, r):
#     for i in range(r):
#         yield tuple(iterable[i] if i < len(iterable) else ' ' for i in range(r))
#
#
#
# data= [1, 2, 3]
# result = my_permutations(data, 2)
#
# for i in result:
#     print(i)


def my_groupby(iterable, function):
    d = {}.fromkeys([len(i) for i in iterable], [])

    for i in iterable:
        d[len(i)] = d.get(len(i)) + [i]
    print(d)



my_groupby(['A', 'B', "DEF", "ZX"], len)

