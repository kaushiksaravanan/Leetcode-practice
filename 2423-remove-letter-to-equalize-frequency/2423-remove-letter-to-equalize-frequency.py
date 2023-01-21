class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq={}
        for i in word:
            if i in freq:
                freq[i]+=1
            if i not in freq:
                freq[i]=1
        d={}
        for i in freq:
            if freq[i] in d:
                d[freq[i]]+=1
            if freq[i] not in d:
                d[freq[i]]=1
        c=0
        ans=[]
        for i in d:
            ans.append([i,d[i]])
            if c>=3:
                return False
            c+=1
        if c==1:
            if ans[0][1]==1:
                return True
            if ans[0][0]==1:
                return True
        if c==2:
            ans.sort()
            freq1=ans[0]
            freq2=ans[1]
            if freq1[0]>2 and freq2[0]>2:
                return False
            if freq1[1]==1:
                if freq1[0]==freq2[0]+1:
                    return True
            if freq2[1]==1:
                if freq2[0]==freq1[0]+1:
                    return True
            if freq1[0]==1 and freq1[1]==1:
                return True
            if freq2[0]==1 and freq2[1]==1:
                return True
        return False