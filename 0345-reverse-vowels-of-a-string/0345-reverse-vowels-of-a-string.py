class Solution:
    def reverseVowels(self, s: str) -> str:
        vov='aeiouAEIOU'
        k=[]
        for i in s:
            if i in vov:
                k.append(i)
        a=''
        for i in s:
            if i in vov:
                a+=k.pop()
            else:
                a+=i
        return a
