class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        def rec(i,j,c):
            print(i,j,c)
            if i>=len(s) or j>=len(t):
                return c
            else:
                if s[i]==t[j]:
                    return rec(i+1,j+1,c+1)
                else:
                    return rec(i+1,j,c)
        k=rec(0,0,0)
        print(k,rec(0,0,0))
        return len(t)-k
        