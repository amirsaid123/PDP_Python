class Solution(object):
    def findEvenNumbers(self, d):
        ans=set()
        for i,j,c in permutations(d,3):
            if i!=0 and c%2==0:
                ans.add(100*i+10*j+c)
        return sorted(ans)






print(Solution().findEvenNumbers([1, 2, 3, 0]))



