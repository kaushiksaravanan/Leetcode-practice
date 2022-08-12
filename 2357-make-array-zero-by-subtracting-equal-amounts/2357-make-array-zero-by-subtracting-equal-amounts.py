def check(nums):
    d=0
    l=0
    for i in nums:
        if i<=0:
            l+=1
        d+=1
    return l!=d
    
    
class Solution:
    def minimumOperations(self,nums):
        l=0
        while check(nums):
            k=99999
            for i in nums:
                if i!=0:
                    k=min(k,i)
            for i in range(len(nums)):
                if nums[i]>0:
                    nums[i]=nums[i]-k
            l+=1
        return l