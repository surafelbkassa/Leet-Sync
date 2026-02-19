class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Map = {}
        heap = []
        ans = []
        for point in points:
            # Map[(point[0]**2+point[1]**2)] = point
            heapq.heappush(heap,((point[0]**2+point[1]**2),point))

        for i in range(k):
            a,b = heapq.heappop(heap)
            ans.append(b)
        return ans