class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_1 = 0
        stone_2 = 0
        reverse_stones = [-x for x in stones]
        heapq.heapify(reverse_stones)
        while len(reverse_stones) > 1:
            stone_1 = -heapq.heappop(reverse_stones)
            stone_2 = -heapq.heappop(reverse_stones)
            
            if stone_1 > stone_2:
                heapq.heappush(reverse_stones, -1 * (stone_1-stone_2))
        return -1 * reverse_stones.pop() if len(reverse_stones) != 0 else 0