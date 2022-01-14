class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        k='aeiouAEIOU'
        curr=s
        reve=s[::-1]
        while i<=j and i<len(s) and j>=0:
            print(i,j)
            if i>=len(s):
                return "".join(curr)
            if curr[i] in k:
                if j<0:
                    return "".join(curr)
                if curr[j] in k:
                    curr[i],curr[j]=curr[j],curr[i]
                    j-=1
                    i+=1
                else:
                    j-=1
                
                    
            else:
                i+=1
                
            # print(curr[i],curr[j])
        return "".join(curr)
            
            
        