map = [
    ["1".center(5,' ') , "2".center(5,' ') , "3".center(5,' ') , "4".center(5,' ')],
    ["🚖".center(5,) , "🚖".center(5,) ,"🚖".center(5,) , "🚖".center(5,)],
    ["9".center(5,' ') , "10".center(5,' ') , "11".center(5,' ') , "12".center(5,' ')],
    ["13".center(5,' ') , "14".center(5,' ') , "15".center(5,' ') , "16".center(5,' ')],
]
columns = "     1  2  3  4"
rows = ['a', 'b', 'c', 'd']

print(columns)

# Qatorlar bilan birga har bir elementni chiqarish
for i, row in enumerate(map):
    print(f" {rows[i]}   " + " ".join(row))
print("")