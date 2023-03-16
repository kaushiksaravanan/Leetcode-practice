class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vov='aeiouAEIOU'
        c=0
        for i in words[left:right+1]:
            if i[-1] in vov and i[0] in vov:
                c+=1
        return c
