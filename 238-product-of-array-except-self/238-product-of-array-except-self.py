class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre_mul=[1]*(n+1)
        suf_mul=[1]*(n+1)
        pre_mul[1]=nums[0]
        for i in range(1,n):
            pre_mul[i+1]=pre_mul[i]*nums[i]
        # print(pre_mul)
        
        for i in range(n-1,-1,-1):
            print(nums[i])
            suf_mul[i]=suf_mul[i+1]*nums[i]
        # suf_mul=suf_mul[:-1]
        print(pre_mul)
        print(suf_mul)
        for i in range(n):
            nums[i]=pre_mul[i]*suf_mul[i+1]
        return nums
            
        
        
        