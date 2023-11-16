class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        rr=len(nums)
        d=set()
        for i in nums:
            d.add(int(i,2))
        for i in range(2**rr):
            if i not in d:
                if i==0:
                    return "0"*rr
                r=bin(i).replace("0b","")
                return "0"*(rr-len(r))+r
        