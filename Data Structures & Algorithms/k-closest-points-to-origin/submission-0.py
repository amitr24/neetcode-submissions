import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heap.append((distance, point))

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(0, k)]