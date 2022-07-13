class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        x=nums[:]
        x.sort()
        # nums.sort()
        y=x[::-1][:k]
        # print(y)
        
        mm=[]
        # print(nums)
        for i in nums:
            # print(i,'dd')
            if i in y:
                # print(i)
                mm.append(i)
                y.remove(i)
        return mm