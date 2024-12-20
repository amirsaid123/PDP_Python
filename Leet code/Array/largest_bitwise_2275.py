class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = []
        for candidate in candidates:
            temp = str(bin(candidate)[2:])
            bits.append(temp)

        max_bit = max(bits, key=len)
        new_bits = []
        for bit in bits:
            temp = bit.rjust(len(max_bit), '0')
            new_bits.append(temp)

        my_list = [list(i) for i in new_bits]

        my_list = list(zip(*my_list))
        maximum = max(my_list, key=lambda x: sum(map(int, x)))

        return sum(map(int, maximum))




from itertools import combinations, permutations, combinations_with_replacement
candidates = [ 8, 8]

bits = []
for candidate in candidates:
    temp = str(bin(candidate)[2:])
    bits.append(temp)


max_bit = max(bits, key=len)
new_bits = []
for bit in bits:
    temp = bit.rjust(len(max_bit), '0')
    new_bits.append(temp)



print(bits)
print(new_bits)

my_list = [list(i) for i in new_bits]


my_list = list(zip(*my_list))
maximum = max(my_list, key=lambda x: sum(map(int,x)))
for row in my_list:
    for col in row:
        print(col, end=' ')
    print()

print(sum(map(int,maximum)))
