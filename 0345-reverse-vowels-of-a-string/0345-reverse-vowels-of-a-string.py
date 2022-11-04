class Solution:
    def reverseVowels(self, s: str) -> str:
        vov='aeiouAEIOU'
        k=''
        l=0
        for i in s:
            if i in vov:
                k+=i
                l+=1
        a=''
        l-=1
        for i in s:
            if i in vov:
                a+=k[l]
                l-=1
            else:
                a+=i
            
        return a
