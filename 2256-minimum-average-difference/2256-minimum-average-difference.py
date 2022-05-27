class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tot_sum=sum(nums)
        # print(tot_sum)
        n=len(nums)
        min_k=999999
        ind=0
        prev_sum=nums[0]
        for i in range(n-1):
            fir_deno=i+1
            last_deno=n-fir_deno
            m=abs(prev_sum//fir_deno-(tot_sum-prev_sum)//last_deno)
            print(m,i,ind)
            if m<min_k:
                min_k=m
                ind=i
            prev_sum+=nums[i+1]
        if min_k>tot_sum//n:
            return n-1
        return ind