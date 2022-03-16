class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        r=[]
        for i in range(len(nums)):
            try:
                r.append(nums[i:].index(key)+i)
            except:
                pass
        r=list(set(r))
        print(r)
        if len(r)>0:
            try:
                k=nums[r[0]+1]
            except:
                pass
            c=0
            d={}
            for i in r:
                try:
                    if nums[i+1] in d:
                        d[nums[i+1]]+=1
                    elif nums[i+1] not in d:
                        d[nums[i+1]]=1
                except:
                    pass
            return sorted(d.items(), key=lambda item: item[1])[::-1][0][0]
            print(k)
        else:
            return 0
            