class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d={}
        l=set()
        for i in logs:
            l.add(tuple(i))
        # logs=set((i) for i in logs)
        for i in l:
            if i[0] in d:
                d[i[0]]+=1
                # d[i[0]]=min(i[1],d[i[0]])
            if i[0] not in d:
                d[i[0]]=1
        a=[0]*k
        print(d)
        for i in d:
            # if d[i]<k:
                a[d[i]-1]+=1
        print(d)
        return a