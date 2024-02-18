class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        count = [0] * n
        
        meetings = sorted(meetings, key= lambda x: x[0])
        
        for meeting in meetings:
            
            pos = self.getOptimalEndTime(meeting[0], rooms)
            
            if pos >= 0 :
                rooms[pos] = meeting[1] 
            else:
                end_time = min(rooms)
                pos = rooms.index(end_time)
                rooms[pos] = rooms[pos] + meeting[1] - meeting[0]

            count[pos] += 1
        
        return count.index(max(count))
            
    def getOptimalEndTime(self, start_time: int, rooms: List[int]) -> int:
        pos = -1
        for index, room in enumerate(rooms):
            if start_time >= room :
                pos = index
                break
        
        return pos