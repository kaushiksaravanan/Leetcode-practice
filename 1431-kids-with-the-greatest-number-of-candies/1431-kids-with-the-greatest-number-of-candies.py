class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        m=max(candies)
        for i in candies:
            if m<=extraCandies+i:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            