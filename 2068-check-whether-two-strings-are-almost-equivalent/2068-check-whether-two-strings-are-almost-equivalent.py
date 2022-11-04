class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        k1={}
        for i in word1:
            if i in k1:
                k1[i]+=1
            if i not in k1:
                k1[i]=1
                
        k2={}
        for i in word2:
            if i in k2:
                k2[i]+=1
            if i not in k2:
                k2[i]=1
        for i in k1:
            if i not in k2:
                if k1[i]>3:
                    return False
            if i in k2:
                if abs(k1[i]-k2[i])>3:
                    return False
        for i in k2:
            if i not in k1:
                if k2[i]>3:
                    return False
            if i in k1:
                if abs(k1[i]-k2[i])>3:
                    return False
        
        return True