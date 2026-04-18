"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []

        for i in intervals:
            events.append((i.start, +1))
            events.append((i.end, -1))
        
        events.sort(key = lambda e: (e[0], e[1]))
        
        currentActiveEvents = 0
        maxActiveEventsAtaMoment = 0

        for time, change in events:
            currentActiveEvents += change
            maxActiveEventsAtaMoment = max(maxActiveEventsAtaMoment, currentActiveEvents)
        
        return maxActiveEventsAtaMoment



        