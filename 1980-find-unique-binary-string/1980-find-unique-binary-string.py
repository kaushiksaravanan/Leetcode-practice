class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        rr=len(nums[0])
        d=[None]*2**rr
        ma=2**rr
        r=2**(rr-1)
        for i in nums:
            d[int(i,2)]=1
        if r==1:
            r-=1
        for i in range(ma):
            if d[i]==None:
                if i==0:
                    return "0"*rr
                r=bin(i).replace("0b","")
                return "0"*(rr-len(r))+r
        