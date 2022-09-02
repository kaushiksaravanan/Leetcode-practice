class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cost=0
        pre=[0]*(len(travel)+1)
        for i in range(len(travel)):
            pre[i+1]=travel[i]+pre[i]
        n1_last=0
        n2_last=0
        n3_last=0
        for i in range(len(garbage)):
            n1=0
            n2=0
            n3=0
            for lett in garbage[i]:
                if lett=='G':
                    n1+=1
                elif lett=='P':
                    n2+=1
                else:
                    n3+=1
            if n1!=0:
                n1_last=i
            if n2!=0:
                n2_last=i
            if n3!=0:
                n3_last=i
            cost=n1+n2+n3+cost
        return cost+pre[n1_last]+pre[n2_last]+pre[n3_last]
        