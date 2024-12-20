elements = [1, 1, 2, 'a', 'b', 'a', '*', '$', '&', '*']
uniques = []
print("Bizning list:", elements)
print()
for element in elements:
    if element not in uniques:
        uniques.append(element)
print("Bir marta takrorlangan elementlar:", uniques)