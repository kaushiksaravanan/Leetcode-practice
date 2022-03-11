class Solution:
    def kthDistinct(self, arr: List[str], m: int) -> str:
        k=[]
        for i in arr:
            if arr.count(i)==1:
                k.append(i)
        print(k)
        try:
            return k[m-1]
        except:
            return ""
                