from collections import deque 
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        total_wins=0
        arr=deque(arr)
        if k>=len(arr):
            return max(arr)
        while total_wins<k:
            # print(arr)
            kr=min(arr[0],arr[1])
            if kr==arr[0]:
                m=arr.popleft()
                arr.append(m)
                total_wins=1
            if kr==arr[1]:
                to_add=arr.popleft()
                m=arr.popleft()
                arr.appendleft(to_add)
                arr.append(m)
                total_wins+=1
                if total_wins==k:
                    return arr[0]

            
        return arr[0]
        