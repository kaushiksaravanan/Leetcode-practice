class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        es=set(s)
        c=0
        # d=set()
        a=0
        for let in es:
                    i,j=s.index(let),s.rindex(let)
                    d=set()
                    for ind in range(i+1,j):
                            d.add(s[ind])
                        # continue
                    a+=len(d)
        print(d)
        return a