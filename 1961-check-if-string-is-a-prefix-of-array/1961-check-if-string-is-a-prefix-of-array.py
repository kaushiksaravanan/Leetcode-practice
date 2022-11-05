class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ind=''
        l=0
        m=len(s)
        for i in words:
            x=0
            for lett in i:
                if len(ind)>=m and x==0:
                    return ind==s
                if len(ind)>=m and x>0:
                    return False
                ind+=lett
                l+=1
                x+=1
        return ind==s
                
        