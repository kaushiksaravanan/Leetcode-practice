class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        print(digits)
        ans=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if digits[i]==0:
                        continue
                    if i==j or j==k or k==i:
                        continue
                    if digits[k]%2==0:
                        ans.add((digits[i]*100)+(digits[j]*10)+digits[k])
        ans=list(ans)
        ans.sort()
        return ans
        