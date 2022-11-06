class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d={}
        r={}
        k=-999999999
        for i in nums:
                d[i]=1
        for i in nums:
            if -i in d:
                k=max(abs(i),k)
                # r[i]=1
        if k==-999999999:
            return -1
        return k
        
        