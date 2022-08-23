class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        m=list(allowed)
        for i in words:
            k=list(set(list(i)))
            l=0
            y=0
            for _ in k:
                if _ in m:
                    y+=1
                l+=1
            if y==l and y!=0 and l!=0:
                c+=1
                print(i)
        return c