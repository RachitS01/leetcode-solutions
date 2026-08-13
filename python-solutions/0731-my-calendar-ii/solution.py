class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.doubleBookings = []


    def book(self, startTime: int, endTime: int) -> bool:
        for db_start,db_end in self.doubleBookings:
            if max(startTime,db_start) < min(endTime,db_end):
                return False

        for b_start,b_end in self.bookings:
            if max(startTime, b_start) < min(endTime,b_end):
                overlapStart = max(startTime,b_start)
                overlapEnd= min(endTime,b_end)

                self.doubleBookings.append([overlapStart,overlapEnd])
        self.bookings.append([startTime,endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
