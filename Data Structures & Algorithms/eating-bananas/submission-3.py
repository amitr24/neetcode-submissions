class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_h = high
        while (low <= high):
            mid = (low + high) // 2
            hours_needed = 0
            for i in piles:
                hours_needed += int(i / mid) + (1 if i % mid > 0 else 0)
            if hours_needed <= h: 
                min_h = min(min_h, mid)
                high = mid - 1
            else:
                low = mid + 1
                
        return min_h