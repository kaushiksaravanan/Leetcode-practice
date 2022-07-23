class Solution:
    def rob(self, nums: List[int]) -> int:
        print(len(nums))
        n=len(nums)
        m=[-1]*200
        def f(n):
            if m[n]!=-1:
                return m[n]
            if n>=len(nums):
                return 0
            n1=nums[n]+f(n+2)
            n2=f(n+1)
            m[n]=max(n1,n2)
            return m[n]
        return f(0)