class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=[]
        a[:]=score
        # for i in range(len(score)):
        #     for j in range(i,len(score)):
        #         if score[i]<score[j]:
        #             t=score[i]
        #             score[i]=score[j]
        #             score[j]=t
        # print(score)
        score.sort()
        score=score[::-1]
        print(a)
        l=[]
        for i in a:
            n=1
            for j in range(len(score)):
                if score[j]==i:
                    if n==1:
                        l.append("Gold Medal")
                    elif n==2:
                        l.append("Silver Medal")
                    elif n==3:
                        l.append("Bronze Medal")
                    else:
                        l.append(str(n))
                n+=1
        print(l)
        return l
                        
                        
            
            