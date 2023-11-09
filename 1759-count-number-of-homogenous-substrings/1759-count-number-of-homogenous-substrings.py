MOD=10**9 + 7
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans=0
        pre=s[0]
        cur=1
        for i in s[1:]:
            if pre==i:
                cur+=1
            if pre!=i:
                ans+=(cur*(cur+1)//2)%MOD
                pre=i
                cur=1
        if cur>0:
            ans+=(cur*(cur+1)//2)%MOD

        return ans