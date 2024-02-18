class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [[0,i] for i in range(n)]
        count = [0] * n
        heapq.heapify(rooms)
        meetings = sorted(meetings, key= lambda x: x[0])
        
        print(meetings)
        
        for start, end in meetings:
            
            while rooms[0][0] < start:
                room_time, room_idx = heapq.heappop(rooms)
                heapq.heappush(rooms,[start, room_idx])
            
            room = heapq.heappop(rooms)
                        
            if room[0] > start:
                room[0] = room[0] + end - start
            else:
                room[0] = end
                
            count[room[1]] += 1
            
            heapq.heappush(rooms, room)
        
        return count.index(max(count))
                
        