class Solution:
    def search(self, A: List[int], target: int) -> int:
        l=0
        h=len(A)-1
        while l<=h:
            #print(l,h)
            mid=(l+h)//2
            if A[mid]==target:
                return mid
            # left half sorted
            if A[mid]>=A[l]:
                if A[l]<=target<=A[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if A[mid]<=target<=A[h]:
                    l=mid+1
                else:
                    h=mid-1
        return -1