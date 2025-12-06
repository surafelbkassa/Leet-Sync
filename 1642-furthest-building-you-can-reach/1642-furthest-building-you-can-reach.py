class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = []
        n = len(heights)
        for i in range(n-1):
            if heights[i+1]-heights[i] > 0:
                heapq.heappush(diff,-(heights[i+1]-heights[i]))
                bricks -= (heights[i+1]-heights[i])
                if bricks < 0:
                    if ladders > 0:
                        bricks += -heapq.heappop(diff)
                        ladders -= 1
                    else:
                        return i    
        return n-1

        

        