class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cost=0
        pre=[0]
        for i in travel:
                pre.append(pre[-1]+i)
        i=0
        n1_last=0
        n2_last=0
        n3_last=0
        for garb in garbage:
            # travel[l]
            n1=garb.count('G')
            n2=garb.count('P')
            n3=len(garb)-n1-n2
            if n1!=0:
                n1_last=i
            if n2!=0:
                n2_last=i
            if n3!=0:
                n3_last=i
            cost=n1+n2+n3+cost
            i+=1
        return cost+pre[n1_last]+pre[n2_last]+pre[n3_last]
        