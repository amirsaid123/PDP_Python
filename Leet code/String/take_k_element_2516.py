# class Solution:
#     def takeCharacters(self, s: str, k: int) -> int:


s = "aabaaaacaabc"
k = 2
temp = ""
counter = 0


if len(s) > 3 * k:
    s = list(s)
    i = 0
    j = len(s) - 1
    while i <= j and k > 0:

        temp += s[i]
        counter += 1
        if temp.count("a") >= k and temp.count("b") >= k and temp.count("c") >= k:
            k -= 1
        temp += s[j]
        counter += 1
        if temp.count("a") >= k and temp.count("b") >= k and temp.count("c") >= k:
            k -= 1

        i += 1
        j -= 1



    print("Final temp:", temp)
    print("Counter:", counter)
else:
    print(-1)

