class Solution:
    def jump(self, nums: List[int]) -> int:
        d={}
        def f(index):
            if index>=len(nums)-1:
                return 0
            k=999999
            if index in d:
                return d[index]
            for i in range(1,nums[index]+1):
                # if i<len(nums):
                    # if index+i!=index:
                        n1=1+f(index+i)
                        k=min(k,n1)
            d[index]=k
            return k
        m=f(0)
        if m==999999:
            return 0
        return m