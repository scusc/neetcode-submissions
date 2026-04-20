import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        freeRooms = [i for i in range(n)]
        busyRooms = []
        
        heapq.heapify(freeRooms)

        bookingCount = [0] * n

        for start, end in meetings:
            while busyRooms:
                finishTime, roomNumber = heapq.heappop(busyRooms)

                if finishTime <= start:
                    heapq.heappush(freeRooms, roomNumber)
                else:
                    heapq.heappush(busyRooms, (finishTime, roomNumber))
                    break
            
            if freeRooms:
                room = heapq.heappop(freeRooms)
                heapq.heappush(busyRooms, (end, room))
                bookingCount[room] += 1
            
            else:
                earliestEnd, room = heapq.heappop(busyRooms)
                heapq.heappush(busyRooms, (earliestEnd + (end - start), room))
                bookingCount[room] += 1
        
        return bookingCount.index(max(bookingCount))
