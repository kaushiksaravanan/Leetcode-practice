class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        apl='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans=0
        ind=len(columnTitle)-1
        for i in columnTitle:
            print(apl.index(i),26**ind,ind)
            ans+=(26**ind)*(apl.index(i)+1)
#             (26^1)*1+(26^0)*ind
            ind-=1
        return ans
            
        