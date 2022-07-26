class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
                #### woah changing order changes output
            if i not in d:
                d[i]=1
        print(d)
        c=0
        l=0
        for i in d:
            if d[i]%2==0:
                c+=d[i]//2
            else:
                l+=d[i]%2
                # l+=1
                c+=d[i]//2
        return [c,l]
        