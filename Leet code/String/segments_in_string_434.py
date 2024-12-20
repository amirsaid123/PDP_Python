class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split()
        return len(words)




obj = Solution()
print(obj.countSegments('Hello,       my       name      is      world'))




# s = "Hello,   my    name    is    John  "
# words = s.split()
# print(words)


