class Solution:
    def average(self, salary: List[int]) -> float:
        min=99999999
        max=-9999999
        sum=0
        k=0
        for i in salary:
            if i>max:
                max=i
            if i<min:
                min=i
            sum+=i
            k+=1
        return (sum-max-min)/(k-2)
        
        
        