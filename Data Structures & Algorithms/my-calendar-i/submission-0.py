class MyCalendar:
    
    def __init__(self):
        self.calendar = set()
        
    def book(self, startTime: int, endTime: int) -> bool:
        booking = set(range(startTime,endTime))
        overlap = len(self.calendar.intersection(booking))
        if overlap > 0:
            return False
        else:
            self.calendar = self.calendar.union(booking)
            return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)