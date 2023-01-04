class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        k=0
        for i in strs:
            lett=0
            l=0
            for letter in i:
                if letter.isdigit():
                    lett+=1
                l+=1
            if lett==l:
                k=max(k,int(i))
            else:
                k=max(k,l)
        return k