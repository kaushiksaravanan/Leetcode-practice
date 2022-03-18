class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        k=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    k=max(k,nums[j]-nums[i])
                    # print()
        return k
                    
        