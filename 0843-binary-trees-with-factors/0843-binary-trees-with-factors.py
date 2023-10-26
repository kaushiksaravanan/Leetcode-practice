class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        possible=[]
        d={}
        root=[]
        for i in arr:
            d[i]=1
        for i in arr:
            for j in arr:
                k=i*j
                if k in d:
                    possible.append((k,i,j))
        arr.sort()
        print(possible)


        @cache
        def rec(ind):
                k=1
                for v in possible:
                    if v[0]==ind:
                        k+=(rec(v[1])*rec(v[2])) % (10 ** 9 + 7)
                
                # for v in arr:
                #     if v==ind:
                #         k+=1
                
                return k % (10 ** 9 + 7)
                

        k=0
        for i in range(len(arr)):
            print(rec(arr[i]))
            k+=rec(arr[i])
        # return rec(0)
        return k % (10 ** 9 + 7)
                    
        print(possible)

        return 1

        