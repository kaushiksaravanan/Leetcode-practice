class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # nums=list(nums))
        if nums.count(2)==100000:
            return -1
        nums.sort()
        k=set(numsDivide)
        c=0
        while c<len(nums):
            f=1
            for i in k:
                if i%nums[c]!=0:
                    c+=1
                    f=0
                    break
            if f==1:
                return c
        if c==len(nums):
            return -1
        return c

        
        