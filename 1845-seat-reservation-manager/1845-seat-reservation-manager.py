from sortedcontainers import SortedSet
class SeatManager:

    def __init__(self, n: int):
        self.sorted_list = SortedSet() 
        self.n=n
        self.marker=1

    def reserve(self) -> int:
        if self.sorted_list:
            return self.sorted_list.pop(0)
        seat_number=self.marker
        self.marker+=1
        return seat_number
            

    def unreserve(self, seatNumber: int) -> None:
        self.sorted_list.add(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)