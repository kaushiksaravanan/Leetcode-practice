class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        d={}
        def rec(s,first,end):
            if first<=end:
                if first==end:
                    return 1
                else:
                    if (first,end) in d:
                        return d[(first,end)]
                    if s[first]==s[end]:
                        d[(first,end)]=2+rec(s,first+1,end-1)
                        return d[(first,end)]
                    else:
                        d[(first,end)]=max(rec(s,first+1,end),rec(s,first,end-1))
                        return d[(first,end)]
            else:
                return 0
        return rec(s,0,len(s)-1)