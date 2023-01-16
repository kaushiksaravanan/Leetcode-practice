def fre(s):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            if i not in d:
                d[i]=1
        return d
class Solution:            
    def commonChars(self, words: List[str]) -> List[str]:
        a=[]
        curr=fre(words[0])
        for ii in range(1,len(words)):
            m=fre(words[ii])
            temp={}
            for i in m:
                if i in curr:
                    temp[i]=min(curr[i],m[i])
            curr=temp
        s=[]
        for i in curr:
            for k in range(curr[i]):
                s.append(i)
        return s
                    
                
        
        