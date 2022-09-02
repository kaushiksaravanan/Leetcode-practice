class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cost=0
        # for i in garbage:
        #     cost=i.count('G')
        #     travel
        # for i in ['G','P','M']:
        # l=-1
        pre=[0]
        for i in travel:
                pre.append(pre[-1]+i)
        
        for let in ['G','P','M']:
            xx=0
            last=0
            for i in garbage:
                n1=i.count(let)
                if n1!=0:
                    last=xx
                    cost+=n1
                xx+=1
            # print(xx)
            # if last==len(pre):
                # cost+=pre[last-1]
            # else:
            cost+=pre[last]
            # if l!=-1:
            # l+=1
        print(pre)
        # for garb in garbage:
        #     # travel[l]
        #     n1=garb.count('G')
        #     n2=garb.count('P')
        #     n3=len(garb)-n1-n2
        #     print(n1,n2,n3,garb,cost)
        #     cost+=(n1+n2+n3)
        #     if l!=-1:
        #         cost+=travel[l]*(n1+n2+n3)
        #     l+=1
            # l=-1
            # for garb in garbage:
            #     # if garb!='':
            #         cost+=garb.count(i)
            #         cost+=travel[l]
            #     if l!=-1:
            #         cost+=travel[l]
            #     l+=1
            #     # garb=garb.replace(i,'')
        # print(garbage)
        return cost
        