class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        #2when two ants meet the time taken will be interchanges and the result will remain the same
        ans=0
        for i in left:
            ans=max(ans,i)
        for i in right:
            ans=max(ans,n-i)
        return ans

        