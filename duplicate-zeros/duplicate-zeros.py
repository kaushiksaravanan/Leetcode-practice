class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n=len(arr)
        x=[]
        for i in arr:
            if len(x)>=n:
                break
            if i==0:
                x.append(0)
            x.append(i)
        arr[:]=x[:n]
        """
        Do not return anything, modify arr in-place instead.
        """
        