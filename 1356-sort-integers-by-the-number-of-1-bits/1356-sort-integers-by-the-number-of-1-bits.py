class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n=len(arr)
        for i in range(n):
            for j in range(n):
                a=bin(arr[j]).count('1')
                b=bin(arr[i]).count('1')
                if a>b:
                    arr[i],arr[j]=arr[j],arr[i]
        prev=[]
        for i in arr:
                t=[]
                for j in arr:
                    if bin(i).count('1')==bin(j).count('1'):
                        t.append(j)
                t.sort()
                if t not in prev:
                    prev.append(t)
        k=[]
        for i in prev:
            for j in i:
                k.append(j)
        # s=[]
        # for i in prev:
        #     for _ in i:
        #         s.append(i)
        return k