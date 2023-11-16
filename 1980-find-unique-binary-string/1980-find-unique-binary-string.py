class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        d=set()
        rr=len(nums[0])
        for i in nums:
            d.add(int(i,2))
        ma=2**rr
        r=2**(rr-1)
        if r==1:
            r-=1
        for i in range(ma):
            if i not in d:
                if i==0:
                    return "0"*rr
                r=bin(i).replace("0b","")
                return "0"*(rr-len(r))+r
        