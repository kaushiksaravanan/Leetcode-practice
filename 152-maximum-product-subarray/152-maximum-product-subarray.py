class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        t=[1,1]
        res=-999999999999999999
        for i in range(len(nums)):
            print(t)
            # t[0]=
            y=t[0]
            t[0]=max(t[0]*nums[i],nums[i]*t[1],nums[i])
            t[1]=min(y*nums[i],nums[i]*t[1],nums[i])
            res=max(t[0],res)

            # if curr_sum>nums[i]:
            # prod_sum[i]=curr_sum
            # else:
                # prod_sum[i]=nums[i]
        print(t)
        return res