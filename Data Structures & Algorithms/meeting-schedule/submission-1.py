"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        store=sorted(intervals,key=lambda i:i.start)
        for i in range(len(store)-1):
            if store[i].end > store[i+1].start:
                return False
            
        return True 

