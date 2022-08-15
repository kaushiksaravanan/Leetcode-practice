class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def rec(s,first,end):
            if first<=end:
                if first==end:
                    return 1
                else:
                    if s[first]==s[end]:
                        return 2+rec(s,first+1,end-1)
                    else:
                        return max(rec(s,first+1,end),rec(s,first,end-1))
            else:
                return 0
                
        return rec(s,0,len(s)-1)